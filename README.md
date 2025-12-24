# 🏥 Medical Document Assistant (Gemini 2.5 Flash)

A Streamlit-based AI application that helps patients understand their **medical documents** such as blood reports, prescriptions, and test results. Powered by **Google Gemini 2.5 Flash**, the assistant explains medical information in **simple, patient-friendly language**, strictly based on the uploaded document.

---

## ✨ Features

* 📄 Upload medical PDFs (blood reports, prescriptions, lab results)
* 🤖 Powered by Google Gemini 2.5 Flash
* 🧠 Context-aware conversation memory
* 🩺 Explains medical terms in simple language
* 📊 Highlights document statistics
* 🔒 Answers only from the uploaded document
* 💬 Warm, supportive, patient-friendly responses
* ⚠️ Built-in medical disclaimer (no diagnosis or treatment)

---

## 🗂️ Project Structure

```
.
├── brain.py        # Medical document processing & AI logic
├── styl.py         # Streamlit UI and app workflow
├── requirements.txt
├── README.md
```

---

## ⚙️ Requirements

* Python **3.9+**
* Google Gemini API Key

### Required Libraries

```bash
pip install streamlit google-generativeai PyPDF2
```

---

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/medical-document-assistant.git
cd medical-document-assistant
```

2. Run the app:

```bash
streamlit run styl.py
```

3. Open the browser
4. Enter your **Google API key**
5. Upload your medical document and start asking questions

---

## 🧠 How It Works

1. User uploads a medical PDF
2. Text is extracted using PyPDF2
3. A strict system prompt is created from the document
4. Gemini 2.5 Flash explains content in simple language
5. Chat history is maintained for better understanding

If information is missing, the assistant responds:

> *"I cannot find that information in your document."*

---

## 📌 What This App Can Help With

* 🧪 Explaining blood test values
* 💊 Understanding prescriptions and dosage instructions
* 📋 Breaking down medical terminology
* 🔬 Explaining lab and test reports
* 📄 Clarifying medical documents

---

## ⚠️ Medical Disclaimer

This application provides **educational information only**.
It does **not** provide medical diagnosis or treatment.
Always consult your doctor or healthcare provider for medical advice.

---

## 🖥️ Built With

* **Google Gemini 2.5 Flash**
* **Streamlit**
* **PyPDF2**
* **Python**

---

## 📄 License

Open-source project for educational and personal use.

---

## 🙌 Acknowledgments

Powered by **Google Gemini 2.5 Flash**
Built with **Streamlit**

---

🏥 *Understanding medical documents made simple and stress-free.*
