import os
import pdfkit
import argparse

def main():
    parser = argparse.ArgumentParser(description="Convert HTML to PDF")
    parser.add_argument('--input', '-i', help='Path to input HTML file')
    parser.add_argument('--output', '-o', help='Path to output PDF file')

    args = parser.parse_args()

    input_path = args.input
    output_path = args.output

    # Configure pdfkit with your wkhtmltopdf path
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

    # PDF options to handle encoding and formatting properly
    options = {
        'page-size': 'A4',
        'margin-top': '0.6in',
        'margin-right': '0.6in',
        'margin-bottom': '0.6in',
        'margin-left': '0.6in',
        'encoding': "UTF-8",
        'no-outline': None,
        'print-media-type': None,
        'disable-smart-shrinking': None,
        'load-error-handling': 'ignore',
        'load-media-error-handling': 'ignore',
        'disable-external-links': None,
        'disable-forms': None,
        'images': None,
        'enable-local-file-access': None,
        'javascript-delay': '1000'
    }

    try:
        pdfkit.from_file(input_path, output_path, configuration=config, options=options)
        print(f"PDF created successfully: {output_path}")
    except Exception as e:
        print(f"Error creating PDF: {e}")
        print("Make sure the HTML file exists and is valid.")

if __name__ == "__main__":
    main()