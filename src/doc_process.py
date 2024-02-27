import PyPDF2

class PDFProcessor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def process_pdf(self):
        try:
            with open(self.pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)

                num_pages = len(pdf_reader.pages)
               # print(f"Number of pages: {num_pages}")

                all_text = ""
                for page in pdf_reader.pages:
                    all_text += page.extract_text()
                #print(f"\nCombined text from all pages:\n{all_text}")

                #page_num = 2
                #page = pdf_reader.pages[page_num - 1]
                #page_text = page.extract_text()
                #print(f"\nText from page {page_num}:\n{page_text}")



                try:
                    metadata = pdf_reader.metadata
                    if metadata:
                        print("\nMetadata:")
                        for key, value in metadata.items():
                            print(f"{key}: {value}")
                except AttributeError:
                    return "PDF doesn't have accessible metadata."

        except FileNotFoundError:
            return f"Error: PDF file '{self.pdf_path}' not found."

        except Exception as e:
            return f"An error occurred: {e}"
        return all_text
    


    def chunk_text(self, chunk_size):
        """Chunk the extracted text into smaller parts."""
        extracted_text = self.process_text()
        if isinstance(extracted_text, str):
            return [extracted_text[i:i+chunk_size] for i in range(0, len(extracted_text), chunk_size)]
        else:
            return extracted_text

    def process_text(self):
        text = self.process_pdf()

        text = text.replace("\n", "")
        return text




