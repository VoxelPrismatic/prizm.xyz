from browser import document

content = {"OwO WHAT IS THIS?": "This is an empty FAQ because nobody asked any questions yet UwU"}

element = document.getElementById("faq")
for key in content:
    title = document.createElement("DIV")
    text = document.createTextNode(key)
    title.class_name = "header"
    title.append(text)
    element.appendChild(title)
    stuff = document.createElement("DIV")
    text = document.createTextNode("")
    stuff.class_name = "content consect"
    stuff.appendChild(text)
    replace = {'\n':'<br>',
               '<code>':'<span class="mono dark">',
               '</code>':'</span>'}
    for re in replace:
        content[key] = content[key].replace(re, replace[re])
    stuff.innerHTML = changes[key]
    element.appendChild(stuff)
