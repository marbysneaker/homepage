import glob
import os
from jinja2 import Template

all_html_files = glob.glob("contents/*.html")
pages =[]

icons =[{"icon":"http://www.twitter.com","logo":"fa fa-twitter-square"},{"icon":"http://www.facebook.com","logo":"fa fa-facebook-square"},{"icon":"http://www.overstackflow.com","logo":"fa fa-stack-overflow icon-large"},{"icon":"http://www.linkedin.com","logo":"fa fa-linkedin-square icon-large"}]

def create_pages():
    for i in all_html_files:
        file_name = os.path.basename(i)
        name_only, extension = os.path.splitext(file_name)
        pages.append({"output":"docs/"+file_name,"title":name_only,"filename":i})
def render():
    for page in pages:
        content_html = open(page['filename']).read()
        template_html = open("templates/base.html").read()
        template = Template(template_html)
        output = template.render(
        icons = icons,
        pages = pages,
        title = page['title'],
        content = content_html,)
        open(page['output'],"w+").write(output)


