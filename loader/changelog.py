from browser import document as doc, html, window as win
from priz_md import mark
content = eval(open("json/changes.json").read())

doc["labels"].innerHTML = '|'.join(list(content))
element = doc["changes"]
lists = doc["tabby"]

for key in content:
    lists <= html.BUTTON(key, Class = "tabby_link", Id = key)
    element <= html.DIV(mark(content[key])+"<br>", Class = "tabby_sect", Id = "changes_"+key, style={"display": "none"})
win.chng()
