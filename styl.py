import streamlit as st
from brain import PDFChatbot


# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="Medical Document Assistant - AI Helper",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==================== CUSTOM STYLING ====================
def apply_custom_css():
    """Apply custom CSS styling to the Streamlit app."""
    st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            font-weight: bold;
            color: #2e7d32;
            text-align: center;
            margin-bottom: 1rem;
        }
        .chat-message {
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            display: flex;
            flex-direction: column;
        }
        .user-message {
            background-color: #e8f5e9;
            border-left: 4px solid #4caf50;
            color: #1b5e20;
        }
        .assistant-message {
            background-color: #f5f5f5;
            border-left: 4px solid #2196f3;
            color: #0d47a1;
        }
        .stButton>button {
            width: 100%;
        }
        .info-box {
            padding: 1rem;
            background-color: #e3f2fd;
            border-left: 4px solid #2196f3;
            border-radius: 0.5rem;
            margin: 1rem 0;
            color: #0d47a1;
        }
        .warning-box {
            padding: 1rem;
            background-color: #fff3e0;
            border-left: 4px solid #ff9800;
            border-radius: 0.5rem;
            margin: 1rem 0;
            color: #e65100;
        }
    </style>
    """, unsafe_allow_html=True)


# ==================== SESSION STATE INITIALIZATION ====================
def initialize_session_state():
    """Initialize Streamlit session state variables."""
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = None
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'pdf_loaded' not in st.session_state:
        st.session_state.pdf_loaded = False


# ==================== SIDEBAR COMPONENTS ====================
def render_sidebar():
    """Render the sidebar with configuration options."""
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # API Key input
        api_key = st.text_input(
            "Google API Key",
            type="password",
            value="YOUR_GOOGLE_API_KEY_HERE",
            help="Enter your Google Gemini API key"
        )
        
        # PDF file uploader
        pdf_file = st.file_uploader(
            "Upload Medical Document",
            type=['pdf'],
            help="Upload your blood report, prescription, or other medical document"
        )
        
        # Load PDF button
        if st.button("🚀 Load Document", type="primary"):
            handle_pdf_load(api_key, pdf_file)
        
        st.divider()
        
        # Statistics section
        if st.session_state.pdf_loaded:
            render_statistics()
        
        st.divider()
        
        # Instructions
        render_instructions()


def handle_pdf_load(api_key: str, pdf_file):
    """
    Handle PDF loading and chatbot initialization.
    
    Args:
        api_key: Google API key
        pdf_file: Uploaded PDF file
    """
    if not api_key or api_key == "YOUR_GOOGLE_API_KEY_HERE":
        st.error("Please enter a valid API key!")
    elif pdf_file is None:
        st.error("Please upload a medical document!")
    else:
        try:
            with st.spinner("Loading your medical document..."):
                # Save uploaded file temporarily
                with open("temp_pdf.pdf", "wb") as f:
                    f.write(pdf_file.getbuffer())
                
                # Initialize chatbot
                st.session_state.chatbot = PDFChatbot(api_key, "temp_pdf.pdf")
                st.session_state.pdf_loaded = True
                st.session_state.messages = []
                
                # Show success messages
                pdf_info = st.session_state.chatbot.get_pdf_info()
                st.success(f"✅ Document loaded: {pdf_file.name}")
                st.info(f"Document size: {pdf_info['content_length']} characters")
        except Exception as e:
            st.error(f"Error loading document: {str(e)}")


def render_statistics():
    """Render chat statistics in the sidebar."""
    st.subheader("📊 Chat Statistics")
    st.metric("Messages", len(st.session_state.messages))
    st.metric("Document", st.session_state.chatbot.pdf_filename)
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()


def render_instructions():
    """Render usage instructions in the sidebar."""
    st.markdown("""
    ### 💡 How to use:
    1. Enter your Google API key
    2. Upload your medical document (blood report, prescription, etc.)
    3. Click "Load Document"
    4. Ask questions in simple language!
    
    ### ✨ What I can help with:
    - Explain blood test results
    - Clarify prescription instructions
    - Break down medical terms
    - Explain normal vs abnormal values
    
    ### ⚠️ Important:
    This is for educational purposes only. Always consult your doctor for medical advice.
    """)


# ==================== MAIN CHAT AREA ====================
def render_welcome_screen():
    """Render the welcome screen when no PDF is loaded."""
    st.markdown("""
    <div class="info-box">
        <h3>🏥 Welcome to Your Medical Document Assistant!</h3>
        <p>I'm here to help you understand your medical documents in simple, easy-to-understand language.</p>
        <p><strong>I can help explain:</strong></p>
        <ul>
            <li>📋 Blood test reports and lab results</li>
            <li>💊 Prescriptions and medication instructions</li>
            <li>🔬 Medical test results</li>
            <li>📄 Other medical documents</li>
        </ul>
        <p>Please upload your document in the sidebar to get started.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="warning-box">
        <strong>⚠️ Important Medical Disclaimer:</strong><br>
        This assistant provides educational information only and is not a substitute for professional medical advice. 
        Always consult your doctor or healthcare provider for medical decisions, diagnosis, and treatment.
    </div>
    """, unsafe_allow_html=True)


def render_chat_message(role: str, content: str):
    """
    Render a single chat message.
    
    Args:
        role: 'user' or 'assistant'
        content: Message content
    """
    if role == "user":
        st.markdown(f"""
        <div class="chat-message user-message">
            <strong>👤 You:</strong><br>
            {content}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message assistant-message">
            <strong>🏥 Medical Assistant:</strong><br>
            {content}
        </div>
        """, unsafe_allow_html=True)


def render_chat_history():
    """Render all chat messages from history."""
    for message in st.session_state.messages:
        render_chat_message(message["role"], message["content"])


def convert_messages_to_history() -> list:
    """
    Convert session messages to history format for the chatbot.
    
    Returns:
        List of conversation exchanges
    """
    history = []
    for i in range(0, len(st.session_state.messages) - 1, 2):
        if i + 1 < len(st.session_state.messages):
            history.append({
                'user': st.session_state.messages[i]['content'],
                'assistant': st.session_state.messages[i + 1]['content']
            })
    return history


def handle_user_input(prompt: str):
    """
    Handle user input and generate response.
    
    Args:
        prompt: User's question
    """
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    render_chat_message("user", prompt)
    
    # Get bot response
    with st.spinner("Analyzing your document..."):
        history = convert_messages_to_history()
        response = st.session_state.chatbot.ask(prompt, history)
    
    # Add assistant message
    st.session_state.messages.append({"role": "assistant", "content": response})
    render_chat_message("assistant", response)
    
    st.rerun()


def render_chat_interface():
    """Render the main chat interface."""
    # Display chat history
    render_chat_history()
    
    # Chat input
    if prompt := st.chat_input("Ask a question about your medical document..."):
        handle_user_input(prompt)


# ==================== FOOTER ====================
def render_footer():
    """Render the footer."""
    st.divider()
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 1rem;">
        🏥 Medical Document Assistant | Powered by Gemini 2.5 Flash | Built with Streamlit<br>
        <small>For educational purposes only - Not a substitute for professional medical advice</small>
    </div>
    """, unsafe_allow_html=True)


# ==================== MAIN APP ====================
def main():
    """Main application entry point."""
    # Apply styling
    apply_custom_css()
    
    # Initialize session state
    initialize_session_state()
    
    # Render header
    st.markdown('<div class="main-header">🏥 Medical Document Assistant</div>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #666; font-size: 1.1rem;">Understanding Your Medical Documents Made Simple</p>', unsafe_allow_html=True)
    
    # Render sidebar
    render_sidebar()
    
    # Render main content
    if not st.session_state.pdf_loaded:
        render_welcome_screen()
    else:
        render_chat_interface()
    
    # Render footer
    render_footer()


if __name__ == "__main__":
    main()
