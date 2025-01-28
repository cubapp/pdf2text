#!/usr/bin/env python3
import os
from PyPDF2 import PdfReader

def change_extension(filename, new_extension):
    # Remove leading dot from extension if present
    new_extension = new_extension.lstrip('.')

    # Split the filename into name and extension
    base_name = filename.rsplit('.', 1)[0]

    # Return new filename with new extension
    return f"{base_name}.{new_extension}"

def convert_pdf_to_text(pdf_path):
    try:
        # Create a PDF reader object
        reader = PdfReader(pdf_path)

        # Get the output text filename
        txt_path = change_extension(pdf_path, 'txt')

        # Open text file for writing
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            # Get the number of pages
            pages = len(reader.pages)

            # Process each page
            for num in range(pages):
                # Extract text from the page
                text = reader.pages[num].extract_text()

                # Write the text to file with a page separator
                txt_file.write(f"--- Page {num + 1} ---\n")
                txt_file.write(text)
                txt_file.write('\n\n')

        print(f"Successfully converted: {pdf_path} -> {txt_path}")
        return True

    except Exception as e:
        print(f"Error converting {pdf_path}: {str(e)}")
        return False

def main():
    # Get current directory
    current_dir = os.getcwd()

    # Find all PDF files in current directory
    pdf_files = [f for f in os.listdir(current_dir)
                 if f.lower().endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found in the current directory")
        return

    print(f"Found {len(pdf_files)} PDF files")

    # Convert each PDF file
    successful = 0
    failed = 0

    for pdf_file in pdf_files:
        pdf_path = os.path.join(current_dir, pdf_file)
        if convert_pdf_to_text(pdf_path):
            successful += 1
        else:
            failed += 1

    # Print summary
    print("\nConversion complete!")
    print(f"Successfully converted: {successful} files")
    if failed > 0:
        print(f"Failed to convert: {failed} files")

if __name__ == "__main__":
    main()
