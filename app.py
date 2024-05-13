import os
import markdown

def convert_md_to_html(md_file):
    """
    Converts a Markdown file to HTML.
    """
    with open(md_file, 'r', encoding='utf-8') as file:
        md_content = file.read()
        html_content = markdown.markdown(md_content)
    return html_content

def main():
    # Define the folder containing the Markdown files
    folder_path = 'posts'

    # Get a list of all Markdown files in the folder
    md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]

    # Convert each Markdown file to HTML and save it
    for md_file in md_files:
        md_file_path = os.path.join(folder_path, md_file)
        html_content = convert_md_to_html(md_file_path)

        # Create the HTML file name by replacing .md extension with .html
        html_file_path = os.path.splitext(md_file_path)[0] + '.html'

        # Write the HTML content to the HTML file
        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

if __name__ == "__main__":
    main()
