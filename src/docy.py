import PyPDF2

class PDFProcessor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def process_pdf(self):
        try:
            with open(self.pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)

                all_text = ""
                for page in pdf_reader.pages:
                    all_text += page.extract_text()

                metadata = pdf_reader.metadata

        except FileNotFoundError:
            return f"Error: PDF file '{self.pdf_path}' not found."
        
        except Exception as e:
            return f"An error occurred: {e}"
        
        return all_text

    def chunk_text(self, chunk_size):
        """Chunk the extracted text into smaller parts."""
        extracted_text = self.process_pdf()
        if isinstance(extracted_text, str):
            return [extracted_text[i:i+chunk_size] for i in range(0, len(extracted_text), chunk_size)]
        else:
            return extracted_text

