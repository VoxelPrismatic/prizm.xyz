from browser import document

content = {"OwO WHAT IS THIS?": "This is an empty FAQ because nobody asked any questions yet UwU"}

element = document.getElementById("faq")
rep = {'\n':'<br>',
       '<code>':'<span class="mono dark">',
       '</code>':'</span>'}
for key in content:
    title = document.createElement("DIV")
    text = document.createTextNode(key)
    title.class_name = "header"
    title.append(text)
    element.append(title)
    stuff = document.createElement("DIV")
    text = document.createTextNode('~loading~')
    stuff.class_name = "content consect"
    stuff.append(text)
    for re in rep:
        content[key] = content[key].replace(re,rep[re])
    stuff.innerHTML = content[key]
    element.append(stuff)
