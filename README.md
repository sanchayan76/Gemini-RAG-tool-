# 📚 PDF Chatbot with Gemini 2.5 Flash

**PDF Chatbot with Gemini 2.5 Flash** is a Streamlit-based application that allows users to upload a PDF document and ask questions about its contents. The chatbot generates accurate, context-aware answers strictly based on the uploaded document, ensuring zero hallucinations and high factual reliability.

---

## ✨ Features

* 📄 Upload and chat with any PDF document
* 🤖 Powered by Google Gemini 2.5 Flash
* 🔒 Answers strictly limited to PDF content
* 🧠 Conversation memory and context awareness
* 📊 Document statistics (filename, character count)
* 🎨 Clean and modern Streamlit UI
* ❌ No hallucinations or external information

---

## 🗂️ Project Structure

```
.
├── brain.py        # PDF processing and Gemini chatbot logic
├── styl.py         # Streamlit UI and app flow
├── README.md       # Project documentation
```

---

## ⚙️ Requirements

* Python 3.9+
* Google Gemini API Key
* Required libraries:

  * streamlit
  * google-generativeai
  * PyPDF2

Install dependencies:

```bash
pip install streamlit google-generativeai PyPDF2
```

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/pdf-chatbot-gemini.git
cd pdf-chatbot-gemini
```

2. Run the app:

```bash
streamlit run styl.py
```

3. Open the browser, enter your **Google API key**, upload a PDF, and start chatting.

---

## 🧠 How It Works

1. The PDF is uploaded and text is extracted
2. A strict system prompt is created using only the PDF content
3. Gemini 2.5 Flash answers questions based solely on the document
4. Conversation history is preserved for better context

If the answer is not found, the chatbot responds clearly:

> *"I cannot find that information in the document."*

---

## 📌 Use Cases

* Research papers
* Study materials
* Manuals and documentation
* Reports and official documents
* Academic and professional review

---

## 🖥️ Built With

* Google Gemini 2.5 Flash
* Streamlit
* PyPDF2
* Python

---

## 📄 License

This project is open-source and free for educational and personal use.

---

## 🙌 Acknowledgments

Powered by **Google Gemini 2.5 Flash**
Built with **Streamlit**
