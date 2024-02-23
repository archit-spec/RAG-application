import PyPDF2
#from Camelot import Table  # Assuming you have Camelot installed for table extraction

class PDFProcessor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path

    def process_pdf(self):
        try:
            with open(self.pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)

                # Get number of pages
                num_pages = len(pdf_reader.pages)
                print(f"Number of pages: {num_pages}")

                # Extract text from all pages (for basic reading)
                all_text = ""
                for page in pdf_reader.pages:
                    all_text += page.extract_text()
                print(f"\nCombined text from all pages:\n{all_text}")

                # Extract text from specific page (for targeted processing)
                page_num = 2  # Replace with the desired page number (starting from 1)
                page = pdf_reader.pages[page_num - 1]
                page_text = page.extract_text()
                print(f"\nText from page {page_num}:\n{page_text}")

                # Extract table data (if applicable)
                try:
                    tables = Table.from_pdf(self.pdf_path)
                    if tables:
                        print("\nExtracted tables:")
                        for table in tables:
                            print(table.df)  # Print table data as a Pandas DataFrame
                except ImportError:
                    print("Camelot library not installed. Please install for table extraction.")

                # Extract metadata (if available)
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


# Usage example

pdf_processor = PDFProcessor("./87286_92960v00_Decoding_Wireless.pdf")  # Replace with the actual path to your PDF
a =  pdf_processor.process_pdf()

