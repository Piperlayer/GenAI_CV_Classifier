from PyPDF2 import PdfReader

try:
    reader = PdfReader("cv_files/cv_1.pdf")
    number_of_pages = len(reader.pages)

    print(f"Number of pages: {number_of_pages}")

    page = reader.pages[0]
    text = page.extract_text()

    print(f"Page object: {page}")
    print(f"Extracted text:\n{text}")

except Exception as e:
    print(f"An error occurred: {e}")
