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



pdf_processor = PDFProcessor("./87286_92960v00_Decoding_Wireless.pdf")
a =  pdf_processor.process_pdf()
print(a)
