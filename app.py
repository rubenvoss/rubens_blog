import os
import markdown

NAVIGATION_BAR = """
<nav>
    <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
    </ul>
</nav>
"""

FOOTER = """
<footer>
    <ul>
        <li><a href="impressum.html">Impressum</a></li>
        <li><a href="dsgvo.html">Datenschutzerklärung (DSGVO)</a></li>
    </ul>
</footer>
"""

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

        # Add navigation bar at the top
        html_content_with_nav = f"{NAVIGATION_BAR}\n{html_content}"

        # Add footer at the bottom
        html_content_with_footer = f"{html_content_with_nav}\n{FOOTER}"

        # Write the HTML content to the HTML file, overriding the old file
        with open(html_file_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content_with_footer)

if __name__ == "__main__":
    main()
