about = open("contents/about.html").read()
index = open("contents/index.html").read()
projects = open("contents/projects.html").read()
bottom = open("templates/bottom.html").read()
top = open("templates/top.html").read()

new_about = top + about + bottom
open("docs/about.html","w").write(new_about)
new_index = top + index + bottom
open("docs/index.html","w").write(new_index)
new_projects = top + projects + bottom
open("docs/projects.html","w").write(new_projects)

