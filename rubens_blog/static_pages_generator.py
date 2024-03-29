import sys, os
import markdown

def convert_md_to_html(markdown_filepath=None, html_filepath=None):
    if markdown_filepath is None or html_filepath is None:
        print("Filepath for Markdown or HTML missing")
        sys.exit(1)
    markdown_file = open(markdown_filepath, "r")
    html_string = markdown.markdown(markdown_file.read())
    with open(html_filepath, "w") as html_file:
        html_file.write(html_string)

with os.scandir("static/") as static_folder:
    print("Converted Files:")
    for markdown_file in static_folder:
        if markdown_file.name.endswith(".md") and markdown_file.is_file():
            html_filename = markdown_file.name[:-3] + ".html"
            convert_md_to_html(markdown_filepath=markdown_file.path, html_filepath="static/" + html_filename)
            print(markdown_file.name + " -> " + html_filename)