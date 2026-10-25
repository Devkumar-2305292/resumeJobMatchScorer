from pypdf import PdfReader


def extract_pdf_text(pdf_file):
    """
    Extracts text from all pages of a PDF file.
    Returns the extracted text as a single string.
    """

    try:
        reader = PdfReader(pdf_file)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text.strip()

    except Exception:
        return ""