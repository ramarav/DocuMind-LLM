import PyPDF2

def load_text(file):
    text = ""
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    else:
        text = file.read().decode("utf-8")
    return text
