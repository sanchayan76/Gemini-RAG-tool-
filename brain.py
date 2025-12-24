import google.generativeai as genai
from PyPDF2 import PdfReader
from typing import List, Dict


class PDFChatbot:
    """Medical chatbot class that helps patients understand their medical documents."""
    
    def __init__(self, api_key: str, pdf_path: str):
        """
        Initialize the medical chatbot.
        
        Args:
            api_key: Google Gemini API key
            pdf_path: Path to the medical document PDF
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
        Create the medical assistant system prompt.
        
        Returns:
            Formatted system prompt
        """
        return f"""You are a compassionate medical assistant helping patients understand their medical documents: "{self.pdf_filename}".

YOUR ROLE:
You help patients understand blood reports, prescriptions, test results, and other medical documents in simple, easy-to-understand language.

IMPORTANT GUIDELINES:
1. Explain medical terms in simple, patient-friendly language
2. Answer questions using ONLY information from the document below
3. Break down complex medical terminology into everyday words
4. If values are abnormal, explain what that might mean in general terms
5. For prescriptions, explain what medications are for and how to take them
6. Always remind patients to consult their doctor for medical advice and treatment decisions
7. If information is not in the document, clearly state "I cannot find that information in your document"
8. Be empathetic and supportive - medical documents can be confusing and scary
9. give your undestanding of the report in a concise manner
10. Maintain context from previous questions in the conversation
11. answer to any doubt the patient may have
12. point out any critical information in the report that the patient should be aware of

COMMUNICATION STYLE:
- Use simple, everyday language
- Avoid complex medical jargon when possible
- If you must use medical terms, always explain them
- Be warm, supportive, and encouraging
- Show understanding that medical information can be overwhelming

MEDICAL DOCUMENT CONTENT:
{self.pdf_content}

IMPORTANT REMINDER: You are providing educational information only. Always encourage patients to discuss their results and any concerns with their healthcare provider."""
    
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
            history_text += f"Patient: {entry['user']}\n"
            history_text += f"Assistant: {entry['assistant']}\n\n"
        
        return history_text
    
    def ask(self, question: str, history: List[Dict[str, str]]) -> str:
        """
        Ask a question to the medical chatbot.
        
        Args:
            question: Patient's question
            history: Previous conversation history
            
        Returns:
            Assistant's response
        """
        conversation_context = self._format_conversation_history(history)
        
        full_prompt = f"""{self.system_prompt}
{conversation_context}
PATIENT'S CURRENT QUESTION: {question}

Please answer in a warm, supportive way using simple language. Remember to base your answer only on the document content and remind the patient to consult their doctor."""
        
        try:
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    def get_pdf_info(self) -> Dict[str, any]:
        """
        Get information about the loaded medical document.
        
        Returns:
            Dictionary with PDF information
        """
        return {
            'filename': self.pdf_filename,
            'content_length': len(self.pdf_content),
            'char_count': len(self.pdf_content)
        }

