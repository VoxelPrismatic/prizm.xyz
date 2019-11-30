from browser import document as doc, html, window as win
from priz_md import mark
content = eval(open("json/projects.json").read())

element = doc["projs"]

for key in content:
    element <= html.DIV(
        mark(content[key]["nam"])+"<br>", 
        Class = "blue", 
        Id = "projects_"+content[key]["nam"]
    )
    element <= html.DIV(
        mark(content[key]["dsc"])+"<br>", 
        Class = "lgrey"
    )
    element <= html.DIV(
        mark(content[key]["oth"])+"<br>",
        Class = "dgry"
    )
    element <= html.DIV(
        mark(content[key]["lnk"])+"<br>",
        style = {"color": "#ff0088 !important"}
    )
