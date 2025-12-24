📚 PDF Chatbot with Gemini 2.5 Flash

An interactive chatbot that lets you chat with your PDF documents using Google Gemini 2.5 Flash, built with Streamlit.
The chatbot answers questions only from the uploaded PDF, ensuring accurate and hallucination-free responses.

✨ Features

📄 Upload and analyze any PDF document

🤖 AI-powered answers using Gemini 2.5 Flash

🔒 Responses strictly limited to PDF content

🧠 Conversation memory with context awareness

📊 PDF statistics (character count, filename)

🎨 Clean, modern Streamlit UI with custom styling

❌ No hallucinations or external knowledge

🗂️ Project Structure
.
├── brain.py        # Core PDF chatbot logic (Gemini + PDF parsing)
├── styl.py         # Streamlit UI and application logic
├── temp_pdf.pdf    # Temporary file created at runtime
└── README.md       # Project documentation
⚙️ Requirements

Python 3.9+

Google Gemini API key

Required Python packages:

streamlit

google-generativeai

PyPDF2

Install dependencies:

pip install streamlit google-generativeai PyPDF2
🚀 How to Run

Clone the repository

git clone https://github.com/your-username/pdf-chatbot-gemini.git
cd pdf-chatbot-gemini

Run the Streamlit app

streamlit run styl.py

Open the app in your browser

Enter your Google Gemini API key

Upload a PDF and start chatting!

🧠 How It Works

The PDF is uploaded and temporarily saved

Text is extracted using PyPDF2

A strict system prompt is created using the PDF content

Gemini 2.5 Flash answers questions only using that content

Conversation history is preserved for better context

If a question cannot be answered from the PDF, the chatbot clearly responds:

"I cannot find that information in the document."

🔐 Safety & Accuracy Rules

Answers are based only on the uploaded PDF

No assumptions or inferred information

No external knowledge usage

Clear refusal when information is missing

🖥️ Built With

Google Gemini 2.5 Flash

Streamlit

PyPDF2

Python

📌 Use Cases

Research paper Q&A

Study notes and textbooks

Company documents & manuals

Legal or policy document review

Academic and professional workflows

📄 License

This project is open-source and free to use for educational and personal purposes.

🙌 Acknowledgments

Powered by Google Gemini 2.5 Flash
Built with ❤️ using Streamlit
