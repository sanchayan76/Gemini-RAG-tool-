# 📚 PDF Chatbot with Gemini 2.5 Flash

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-green)

**PDF Chatbot with Gemini 2.5 Flash** is a Streamlit-based application that allows users to upload a PDF document and ask questions about its contents. The chatbot provides accurate, context-aware answers strictly based on the uploaded document, ensuring zero hallucinations and high factual reliability.

---

## ✨ Features

* 📄 Upload and chat with any PDF document
* 🤖 Powered by Google Gemini 2.5 Flash
* 🔒 Answers strictly limited to PDF content
* 🧠 Conversation memory and context awareness
* 📊 Document statistics (filename, character count)
* 🎨 Clean and modern Streamlit UI
* ❌ No hallucinations or external knowledge

---

## 🗂️ Project Structure

```
.
├── brain.py        # PDF processing and Gemini chatbot logic
├── styl.py         # Streamlit UI and app flow
├── requirements.txt
├── README.md
```

---

## ⚙️ Requirements

* Python **3.9+**
* Google Gemini API Key

Install dependencies:

```bash
pip install -r requirements.txt
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

1. Upload a PDF document
2. Text is extracted using PyPDF2
3. A strict system prompt is created using only the PDF content
4. Gemini 2.5 Flash answers questions based solely on the document
5. Conversation history is maintained for better context

If an answer does not exist in the document, the chatbot responds:

> *"I cannot find that information in the document."*

---

## 📌 Use Cases

* Research papers
* Study materials
* Manuals & documentation
* Reports and official files
* Academic and professional review

---

## 🖥️ Built With

* **Google Gemini 2.5 Flash**
* **Streamlit**
* **PyPDF2**
* **Python**

---

## 📄 License

Open-source and free for educational and personal use.

---

## 🙌 Acknowledgments

Powered by **Google Gemini 2.5 Flash**
Built with **Streamlit**
