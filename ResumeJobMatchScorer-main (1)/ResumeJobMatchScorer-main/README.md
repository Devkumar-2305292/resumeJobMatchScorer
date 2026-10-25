# 📄 Resume Job Match Scorer

An AI-powered Resume Job Match Scorer built using Python, Streamlit, and Google's Gemini API.
The application compares a candidate's resume with a job description and generates an ATS-style analysis including:
- ATS Match Score
- Matched Skills
- Missing Skills
- Strengths
- Weaknesses
- Suggestions

---

## Features
- Upload Resume PDF
- Upload Job Description PDF
- Paste Job Description
- Automatic PDF text extraction
- AI-powered ATS analysis using Gemini
- Download analysis report
- Clean and responsive Streamlit interface

---

## Tech Stack
- Python 3.10+
- Streamlit
- Google Gemini API
- PyPDF

---

## Project Structure
```
ResumeJobMatchScorer/
│
├── .streamlit/
│   └── secrets.toml
│
├── app.py
├── gemini_helper.py
├── pdf_helper.py
├── prompts.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository (or download and extract the project folder if you didn't get it from GitHub):
```bash
git clone <repository-url>
cd ResumeJobMatchScorer
```

Create and activate a virtual environment (recommended):
```bash
# conda
conda create -n resumematcher python=3.11
conda activate resumematcher

# or venv
python -m venv resumematcher
# Windows
.\resumematcher\Scripts\Activate.ps1
# Mac/Linux
source resumematcher/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Configure Gemini API

Create the following file:
```
.streamlit/secrets.toml
```

Add your API key:
```toml
GEMINI_API_KEY = "YOUR_API_KEY"
```

You can generate a free API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Do not commit this file** — it's already excluded via `.gitignore`.

---

## Run the Project
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## How It Works
1. Upload a Resume PDF.
2. Upload a Job Description PDF or paste the job description.
3. The application extracts text from the uploaded documents.
4. Gemini analyzes the resume against the job description.
5. The application displays:
   - ATS Match Score
   - Matched Skills
   - Missing Skills
   - Strengths
   - Weaknesses
   - Suggestions
6. Download the generated analysis as a text file.

---

## Example Output

```
ATS Match Score: 82%

Matched Skills:
- Python
- REST API Development
- Problem-Solving / Algorithmic Thinking

Missing Skills:
- Kubernetes
- GraphQL

Strengths:
- Strong hands-on project experience with measurable impact
- Clear alignment with the role's core technical requirements

Weaknesses:
- Limited exposure to cloud infrastructure tools mentioned in the JD

Suggestions:
- Highlight any cloud-related coursework or side projects
- Quantify project outcomes wherever possible
```

---

## Notes
- The app uses `gemini-3.1-flash-lite` by default, which is free-tier eligible. If Google changes free-tier model availability, update `MODEL_NAME` in `gemini_helper.py`.
- If a PDF is scanned/image-only (no selectable text), extraction will fail and the app will show a clear error instead of silently sending empty text to the model.
- Free-tier API keys have daily/per-minute rate limits. If you hit a `429` error, wait a bit or check your quota in Google AI Studio.

---

## Future Improvements
- Support scanned PDFs using OCR
- Export analysis as PDF
- Resume keyword highlighting
- Improved ATS scoring logic

---

## License
This project is licensed under the MIT License.

---

## Author
Sidhant Sahni