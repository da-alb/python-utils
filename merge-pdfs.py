import PyPDF2
import os

def merge_pdfs_in_folder(folder_path, output_path):
    """Merges all PDF files in a folder into a single PDF.

    Args:
        folder_path: The path to the folder containing the PDF files.
        output_path: The path to save the merged PDF.
    """

    pdf_merger = PyPDF2.PdfMerger()
    pdf_files = []

    try:
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(".pdf"):  # Check for .pdf extension (case-insensitive)
                filepath = os.path.join(folder_path, filename)
                pdf_files.append(filepath)
    except FileNotFoundError:
        print(f"Error: Folder not found: {folder_path}")
        return
    except NotADirectoryError:
        print(f"Error: {folder_path} is not a directory.")
        return
    except Exception as e: #catch any other exceptions
        print(f"An unexpected error occurred: {e}")
        return


    if not pdf_files:  # Check if any PDF files were found
        print(f"No PDF files found in: {folder_path}")
        return

    pdf_files.sort() #sort files alphabetically

    for path in pdf_files:
        try:
            with open(path, 'rb') as pdf_file:
                pdf_merger.append(pdf_file)
        except Exception as e:
            print(f"Error processing file {path}: {e}")
            return

    try:
        with open(output_path, 'wb') as output_file:
            pdf_merger.write(output_file)
        print(f"Successfully merged PDFs in {folder_path} into {output_path}")
    except Exception as e:
            print(f"Error writing merged PDF: {e}")
            return


if __name__ == "__main__":
    folder_to_merge = "pdfs"  # Replace with the actual folder path
    output_pdf_file = "merge.pdf"  # Replace with the desired output path

    merge_pdfs_in_folder(folder_to_merge, output_pdf_file)