import markdown
import argparse

def main():
    parser = argparse.ArgumentParser(description='Convert markdown file to HTML')
    parser.add_argument('--input', '-i', help='Path to input markdown file')
    parser.add_argument('--output', '-o', help='Path to output HTML file')

    args = parser.parse_args()

    input_path = args.input
    output_path = args.output

    with open(input_path, "r", encoding='utf-8') as f:
        md = f.read()

    html = markdown.markdown(md)

    with open(output_path, "w", encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    main()

# Also, you can add styling like such afterwards.
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Your Name - Resume</title>
#     <style>
#         body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }
#         h1 { color: #333; border-bottom: 2px solid #333; }
#         h2 { color: #666; margin-top: 30px; }
#         h3 { color: #888; }
#         a { color: #0066cc; text-decoration: none; }
#         a:hover { text-decoration: underline; }
#         ul { margin: 10px 0; }
#         li { margin: 5px 0; }
#         hr { border: none; border-top: 1px solid #ddd; margin: 20px 0; }
#     </style>
# </head>