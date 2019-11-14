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

# combing contents and template
def add_content():
    new_content = []
    for page in pages:        
        template = open("templates/base.html").read()
        content = open(page['filename']).read()
        final_projects = template.replace("{{content}}", content)
        new_content.append(final_projects)
    return new_content


#changing title
def add_title():
    final = []
    new_pages= add_content()
    titles = ["Resume / About page","Resume / Projects page","Resume  / Blog page"]
    for i in range(0,3):
        title_added = new_pages[i].replace("{{title}}",titles[i])
        final.append(title_added)
    return final

#writing the new file
def main(final):
    x = 0
    for i in final:
        open(pages[x]['output'],"w+").write(i)
        x += 1
    print(len(final))

    
            

    

        
if __name__ == "__main__":
    add_content()
    add_title()
    final = add_title()
    main(final)
   

