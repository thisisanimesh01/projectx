# ⚖️ Legal Document Assistant

An AI-powered web application that allows users to upload legal documents (PDFs) and instantly get a summarized version along with answers to custom questions.

![App Screenshot](static/assistant/img.png)
---

## 🚀 Features

- 📄 Upload PDF legal documents
- 🧠 Automatic document summarization
- ❓ Ask questions related to the document
- ⚡ Fast AI-powered responses
- 🌐 Simple and clean UI

---

## 🛠️ Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS
- **AI Integration:** OpenRouter (Mistral / LLM APIs)
- **PDF Processing:** PyPDF2 / pdfplumber

---

## 📂 Project Structure

```id="8h8lgx"
legal_ai_assistant/
│
├── ai_core/              # LLM integration (OpenRouter, prompts, parser)
├── assistant/            # Django app (views, models, forms)
├── templates/            # HTML templates
├── static/               # CSS, JS, images
├── media/                # Uploaded files
├── manage.py
└── db.sqlite3
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash id="7ip1jz"
git clone https://github.com/thisisanimesh01/Legal_Document_Assistant.git
cd Legal_Document_Assistant
```

---

### 2️⃣ Create Virtual Environment

```bash id="i6o9fr"
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash id="wdy3ir"
pip install -r requirements.txt
```

---

### 4️⃣ Set Environment Variables

Create a `.env` file in the root directory:

```
OPENROUTER_API_KEY=your_api_key_here
```

---

### 5️⃣ Run Migrations

```bash id="5nyf3p"
python3 manage.py makemigrations
python3 manage.py migrate
```

---

### 6️⃣ Start Server

```bash id="fsv3m6"
python3 manage.py runserver
```

Visit:
👉 http://127.0.0.1:8000/

---

## 🧠 How It Works

1. User uploads a legal document
2. Text is extracted using parsing modules
3. Content is sent to LLM via OpenRouter
4. AI returns:

   * Summary
   * Answers to user queries

---

## 🎯 Use Cases

* Legal professionals
* Law students
* Contract analysis
* Quick legal document understanding

---

## 🔮 Future Improvements

* Multi-language support
* Voice-based legal assistant
* Deployment (AWS / Docker)
* Advanced clause detection

---

## 🤝 Contributing

```bash id="0w85a7"
fork → clone → branch → commit → push → PR
```

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Animesh Yadav**
AI/ML Developer | Django Developer

---

## ⭐ Support

If you found this useful:

* ⭐ Star this repo
* 🍴 Fork it
* 🚀 Share it

---

🔥 *Simplifying legal complexity using AI + LLMs*
