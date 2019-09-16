from browser import document
changes = {""}

changelog = document.getElementById("about")
for key in changes:
    date = document.createElement("DIV")
    text = document.createTextNode(key)
    date.class_name = "header"
    date.append(text)
    changelog.appendChild(date)
    
    changed = document.createElement("DIV")
    text = document.createTextNode("")
    changed.class_name = "content consect"
    changed.appendChild(text)
    replace = {'\n':'<br>',
               '<code>':'<span class="mono dark">',
               '</code>':'</span>'}
    for re in replace:
        changes[key] = changes[key].replace(re, replace[re])
    changed.innerHTML = changes[key]
    changelog.appendChild(changed)
