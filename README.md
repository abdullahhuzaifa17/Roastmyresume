# 🔥 Savage Resume Roaster

**Your resume deserves the truth. Even if it hurts. 💀**

Savage Resume Roaster is an AI-powered web application that analyzes PDF resumes and delivers witty, sarcastic, and brutally honest feedback with a recruiter's perspective.

Built using **Python, Streamlit, LangChain, and Groq**, the application extracts text from uploaded PDF resumes and uses a large language model to identify weaknesses, mock generic buzzwords, evaluate resume quality, and suggest practical improvements.

## ✨ Features

- 📄 **PDF Resume Upload:** Upload a resume directly through the Streamlit interface.
- 🤖 **AI-Powered Analysis:** Uses LangChain and Groq to analyze resume content.
- 🔥 **Savage Resume Roast:** Get humorous, sarcastic, and constructive feedback.
- 💀 **Weakness Detection:** Identify vague claims, generic buzzwords, and weak descriptions.
- 📊 **Resume Score:** Receive a score out of 10 with an explanation.
- 🛠️ **Actionable Improvements:** Get three practical suggestions to improve your resume.
- 🎯 **Recruiter Perspective:** Focuses on experience, achievements, skills, and presentation.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Web interface and PDF upload |
| LangChain | LLM integration |
| `langchain-groq` | Connects LangChain to Groq |
| Groq API | Runs the language model |
| `pypdf` | Extracts text from PDF files |
| `python-dotenv` | Loads API credentials from `.env` |

## 📁 Project Structure

```text
savage-resume-roaster/
├── app.py          # Streamlit user interface
├── roast.py        # Groq connection and resume analysis
├── .env            # API key (not committed to GitHub)
├── .gitignore      # Files excluded from Git
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/abdullahhuzaifa17/Roastmyresume.git
cd savage-resume-roaster
```

Replace `abdullahhuzaifa17` with your GitHub username.

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it:

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```cmd
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Alternatively, install them directly:

```bash
pip install streamlit langchain-groq pypdf python-dotenv
```

### 4. Configure your Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get an API key from the [Groq Console](https://console.groq.com/keys).

**Security:** Never commit your `.env` file or expose your API key publicly.

### 5. Run the application

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open it in your browser to start roasting resumes.

## 🚀 How to Use

1. Launch the application.
2. Upload a resume in PDF format.
3. Click **Roast My Resume**.
4. Wait while the application extracts the text and analyzes the resume.
5. Read the generated roast and improvement suggestions.

## 🔍 How It Works

1. The user uploads a PDF through the Streamlit interface in `app.py`.
2. The app passes the uploaded file to `indexpdf()` in `roast.py`.
3. `pypdf` extracts text from the PDF pages.
4. LangChain sends the extracted text and roasting instructions to the Groq-hosted model.
5. The model generates feedback.
6. Streamlit displays the response.

## 🎭 Roast Format

The AI is instructed to provide six sections:

1. 🔥 **Opening Roast** — A hilarious first impression.
2. 💀 **Biggest Flaws** — Specific weaknesses and red flags.
3. 🤡 **Buzzword Roast** — A critique of generic corporate jargon.
4. 📊 **Resume Score** — A score out of 10 with reasoning.
5. 🛠️ **Top 3 Fixes** — Practical improvements with examples.
6. ☠️ **Final Kill Shot** — An unforgettable closing punchline.

The goal is to roast the resume, not the person, while providing useful career feedback.

## ⚠️ Limitations

- **PDF support:** The current implementation accepts PDF files only.
- **Scanned PDFs:** Image-based PDFs may require OCR because `pypdf` extracts text rather than recognizing text in images.
- **Model availability:** The configured Groq model must be available to your API account.
- **API limits:** Requests are subject to Groq rate limits and usage restrictions.
- **AI accuracy:** Generated feedback can be imperfect. Review recommendations before making career decisions.
- **Privacy:** Resume content is sent to the configured AI provider for analysis. Avoid uploading confidential information unless you are comfortable with the provider's data-handling policies.

## 🔐 Security

- Store credentials in `.env`.
- Never hardcode API keys in source files.
- Never commit `.env` to GitHub.
- Review your repository for secrets before pushing.

## 🗺️ Future Improvements

- [ ] Add professional feedback mode.
- [ ] Support scanned PDFs using OCR.
- [ ] Add resume section detection.
- [ ] Export feedback as a downloadable PDF.
- [ ] Add job-description matching.
- [ ] Add resume improvement suggestions with rewritten bullet points.
- [ ] Improve error handling and PDF validation.
- [ ] Deploy the application online.

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## 📄 License

This project is intended for educational and personal development purposes. Add a license file, such as an MIT License, if you want others to use, modify, and distribute the project under those terms.

---

**Built with Python, Streamlit, LangChain, and Groq.**

*Your resume gets roasted. Your career gets a chance to level up.* 🔥