# 📄 Resume Job Match Scorer

An AI-powered application built with **Python, Streamlit, and Google's Gemini API** that compares a candidate's resume with a job description and generates an ATS-style analysis with actionable feedback.

## ✨ Features

- 📄 Upload a resume in PDF format
- 📑 Upload a job description PDF or paste the description directly
- 🔍 Automatically extract text from PDF documents
- 🤖 Generate AI-powered resume-to-job analysis using Gemini
- 📊 View an ATS-style match score
- ✅ Identify matched and missing skills
- 💡 Discover strengths, weaknesses, and improvement suggestions
- 📥 Download the generated analysis report
- 🎨 Use a clean, responsive Streamlit interface

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit** — interactive web interface
- **Google Gemini API** — AI-powered resume analysis
- **PyPDF** — PDF text extraction

## 📂 Project Structure

```text
ResumeJobMatchScorer/
├── .streamlit/
│   └── secrets.toml
├── app.py
├── gemini_helper.py
├── pdf_helper.py
├── prompts.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ResumeJobMatchScorer
```

Replace `<repository-url>` with your actual GitHub repository URL.

### 2. Create a Virtual Environment

Using Python's built-in `venv`:

**Windows PowerShell**

```powershell
python -m venv resumematcher
.\resumematcher\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv resumematcher
source resumematcher/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Configure the Gemini API

1. Generate an API key through [Google AI Studio](https://aistudio.google.com/apikey).
2. Create a `.streamlit/secrets.toml` file in the project directory.
3. Add the following configuration:

```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your actual API key.

**Security note:** Never commit your API key or `secrets.toml` file to a public repository. Keep it excluded through `.gitignore`.

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

`http://localhost:8501`

## 🔄 How It Works

1. **Upload documents:** Provide a resume PDF and a job description PDF, or paste the job description.
2. **Extract text:** PyPDF extracts available text from the uploaded documents.
3. **Analyze content:** The application sends the extracted text and analysis instructions to the Gemini API.
4. **Generate insights:** The application produces an ATS-style match score, matched skills, missing skills, strengths, weaknesses, and suggestions.
5. **Review results:** View the analysis through the Streamlit interface.
6. **Download report:** Export the generated analysis as a text file.

## 📊 Example Output

The following is an illustrative example of the type of analysis the application can generate:

```text
ATS Match Score: 82%

Matched Skills:
- Python
- REST API Development
- Problem-Solving / Algorithmic Thinking

Missing Skills:
- Kubernetes
- GraphQL

Strengths:
- Relevant hands-on project experience
- Alignment with core technical requirements

Weaknesses:
- Limited exposure to cloud infrastructure tools

Suggestions:
- Highlight relevant cloud-related coursework or projects
- Quantify project outcomes wherever possible
```

*The score and feedback above are illustrative and do not represent a validated or official ATS score.*

## 📝 Notes and Limitations

- The application uses `gemini-3.1-flash-lite` by default, as specified in the project configuration. Model availability and free-tier quotas may change; check the current Gemini API documentation if requests fail.
- Text extraction may fail for scanned or image-only PDFs because they require optical character recognition (OCR).
- Gemini API requests may encounter rate limits. Handle errors appropriately and check your API quota if you receive a `429` response.
- AI-generated match scores are estimates and may not reflect the scoring rules of a specific applicant tracking system.

## 🚀 Future Improvements

- Add OCR support for scanned PDFs
- Export analysis reports as PDF
- Highlight relevant and missing keywords directly in the resume
- Develop a more systematic, validated scoring mechanism
- Add input validation and improved error handling
- Evaluate output consistency across different resumes and job descriptions

## 📜 License

This project is intended to use the **MIT License**. Include a `LICENSE` file containing the actual MIT license text before claiming that the repository is formally licensed under it.

## 👨‍💻 Author

**Dev Kumar**

- GitHub: [Devkumar-2305292](https://github.com/Devkumar-2305292)
- LinkedIn: [Dev Kumar](https://www.linkedin.com/in/dev-kumar-0578402aa/)
