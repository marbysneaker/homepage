
pages = [{
    "filename": "contents/about.html",
    "output": "docs/about.html",
    "title": "About Me"},
    {"filename": "contents/projects.html",
    "output": "docs/projects.html",
    "title": "My Projects"},
    {"filename": "contents/index.html",
    "output": "docs/index.html",
    "title": "Blog"}]

def main():
    for page in pages:
        if page['title']== 'About Me':
            template = open("templates/base.html").read()       
            content = open(page['filename']).read()
            final_about = template.replace("{{content}}", content)
            final_about = final_about.replace("{{title}}", "Resume  / About page")
        return open(page['output'],"w+").write(final_about,)
   
def projects():
    for page in pages:
        if page['title']== "My Projects":
            template = open("templates/base.html").read()
            content = open(page['filename']).read()
            final_projects = template.replace("{{content}}", content)
            final_projects = final_projects.replace("{{tilte}}", "Resume  / Projects page")
            return open(page['output'],"w+").write(final_projects)

def blog():
    for page in pages:
        if page['title']== "Blog":
            template = open("templates/base.html").read()
            content = open(page['filename']).read()
            final_blog = template.replace("{{content}}", content)
            final_blog = final_blog.replace("{{tilte}}", "Resume  / Blog page")
            return open(page['output'],"w+").write(final_blog)
        

            

if __name__ == "__main__":
    main()
    projects()
    blog()



    # about = open("contents/about.html").read()
    # index = open("contents/index.html").read()
    # projects = open("contents/projects.html").read()
    # bottom = open("templates/bottom.html").read()
    # top = open("templates/top.html").read()

    # new_about = top + about + bottom
    # open("docs/about.html","w").write(new_about)
    # new_index = top + index + bottom
    # open("docs/index.html","w").write(new_index)
    # new_projects = top + projects + bottom
    # open("docs/projects.html","w").write(new_projects)