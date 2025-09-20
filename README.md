# Resume Optimizer

A Python tool that automatically optimizes your resume for specific job descriptions using AI, then converts it to HTML and PDF formats.

## Features

- 🤖 **AI-Powered Optimization**: Uses OpenAI GPT to tailor your resume for specific job descriptions
- 📝 **Markdown Support**: Works with markdown-formatted resumes
- 🌐 **HTML Export**: Converts optimized resumes to clean HTML
- 📄 **PDF Generation**: Creates professional PDFs from HTML
- 🎨 **Customizable Styling**: Easy to add custom CSS styling to HTML output
- ⚙️ **Command Line Interface**: Flexible command-line arguments for custom file paths

## Installation

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd resumeOptimizer
   ```

2. Install dependencies:
   ```bash
   pip install openai markdown pdfkit
   ```

3. Install wkhtmltopdf (required for PDF generation):
   - **Windows**: Download from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html)
   - **Linux**: `sudo apt install wkhtmltopdf`
   - **macOS**: `brew install wkhtmltopdf`

4. Set your OpenAI API key:
   ```bash
   # Windows
   set OPENAI_API_KEY=your_api_key_here
   
   # Linux/macOS
   export OPENAI_API_KEY=your_api_key_here
   ```

## Usage

### Basic Workflow (uses default files):
```bash
python optimizer.py
python exporter_md2html.py
python exporter_html2pdf.py
```

### Custom Files:
```bash
python optimizer.py --resume your_resume.md --job job_description.txt --output optimized_resume.md
python exporter_md2html.py --input optimized_resume.md --output resume.html
python exporter_html2pdf.py --input resume.html --output resume.pdf
```

### Help:
```bash
python optimizer.py --help
python exporter_md2html.py --help
python exporter_html2pdf.py --help
```

## File Structure

```
resumeOptimizer/
├── optimizer.py              # AI-powered resume optimization
├── exporter_md2html.py       # Markdown to HTML conversion
├── exporter_html2pdf.py      # HTML to PDF conversion
├── resumes/                  # Input/output resume files
├── job_descriptions/         # Job description files
├── HTMLs/                    # Generated HTML files
└── PDFs/                     # Generated PDF files
```

## Customizing HTML Styling

The HTML output can be easily customized by modifying the generated HTML file or adding CSS. Here's an example of professional styling you can add:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Name - Resume</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }
        h1 { color: #333; border-bottom: 2px solid #333; }
        h2 { color: #666; margin-top: 30px; }
        h3 { color: #888; }
        a { color: #0066cc; text-decoration: none; }
        a:hover { text-decoration: underline; }
        ul { margin: 10px 0; }
        li { margin: 5px 0; }
        hr { border: none; border-top: 1px solid #ddd; margin: 20px 0; }
    </style>
</head>
<body>
    <!-- Your resume content here -->
</body>
</html>
```

## Scripts

- **`optimizer.py`**: Analyzes job descriptions and optimizes your resume using AI
- **`exporter_md2html.py`**: Converts markdown resumes to HTML format
- **`exporter_html2pdf.py`**: Converts HTML resumes to PDF format

## Requirements

- Python 3.6+
- OpenAI API key
- wkhtmltopdf (for PDF generation)

## License

MIT License - feel free to use and modify as needed.