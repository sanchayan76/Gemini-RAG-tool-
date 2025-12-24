
import google.generativeai as genai
from PyPDF2 import PdfReader
from typing import List, Dict


class PDFChatbot:
    """Main chatbot class that handles PDF processing and question answering."""
    
    def __init__(self, api_key: str, pdf_path: str):
        """
        Initialize the PDF chatbot.
        
        Args:
            api_key: Google Gemini API key
            pdf_path: Path to the PDF file
        """
        # Configure Gemini API
        genai.configure(api_key=api_key)
        
        # Initialize model (Gemini 2.5 Flash)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Extract PDF content
        self.pdf_content = self._extract_pdf_text(pdf_path)
        self.pdf_filename = pdf_path.split('/')[-1].split('\\')[-1]
        
        # System prompt
        self.system_prompt = self._create_system_prompt()
    
    def _extract_pdf_text(self, pdf_path: str) -> str:
        """
        Extract text content from PDF file.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Extracted text content
        """
        try:
            reader = PdfReader(pdf_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n\n"
            return text.strip()
        except Exception as e:
            raise Exception(f"Error reading PDF: {str(e)}")
    
    def _create_system_prompt(self) -> str:
        """
        Create the system prompt with instructions.
        
        Returns:
            Formatted system prompt
        """
        return f"""You are a helpful assistant that answers questions based ONLY on the following PDF document: "{self.pdf_filename}".

IMPORTANT RULES:
1. Answer questions using ONLY information found in the document below
2. If the answer is not in the document, clearly state "I cannot find that information in the document"
3. Do not make up or infer information that is not explicitly stated
4. Maintain context from previous questions in the conversation
5. Be specific and cite relevant parts when answering
6. If asked about something outside the document scope, politely redirect to document-based questions

DOCUMENT CONTENT:
{self.pdf_content}

Remember: Never generate information beyond what's in the document above."""
    
    def _format_conversation_history(self, history: List[Dict[str, str]]) -> str:
        """
        Format conversation history for context.
        
        Args:
            history: List of conversation exchanges
            
        Returns:
            Formatted conversation history string
        """
        if not history:
            return ""
        
        history_text = "\n\nPREVIOUS CONVERSATION:\n"
        for entry in history[-5:]:  # Last 5 exchanges
            history_text += f"User: {entry['user']}\n"
            history_text += f"Assistant: {entry['assistant']}\n\n"
        
        return history_text
    
    def ask(self, question: str, history: List[Dict[str, str]]) -> str:
        """
        Ask a question to the chatbot.
        
        Args:
            question: User's question
            history: Previous conversation history
            
        Returns:
            Assistant's response
        """
        conversation_context = self._format_conversation_history(history)
        
        full_prompt = f"""{self.system_prompt}
{conversation_context}
CURRENT QUESTION: {question}

Please answer based only on the document content above."""
        
        try:
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def get_pdf_info(self) -> Dict[str, any]:
        """
        Get information about the loaded PDF.
        
        Returns:
            Dictionary with PDF information
        """
        return {
            'filename': self.pdf_filename,
            'content_length': len(self.pdf_content),
            'char_count': len(self.pdf_content)
        }