from priz_md import *
from browser import document as doc, html

ls = doc.select(".var")
for el in ls:
    doc <= html.DIV(el.innerHTML.split(':')[1], Id = el.innerHTML.split(':')[0])
    el.innerHTML = ""

ls = doc.select(".markall")
for el in ls:
    el.innerHTML = mark(el.innerHTML)

ls = doc.select(".markinit")
for el in ls:
    el.innerHTML = init(el.innerHTML)

ls = doc.select(".markelem")
for el in ls:
    el.innerHTML = elem(init(el.innerHTML))

ls = doc.select(".marklink")
for el in ls:
    el.innerHTML = link(init(el.innerHTML))
    
ls = doc.select(".markbasic")
for el in ls:
    el.innerHTML = basic(init(el.innerHTML))

ls = doc.select(".markadvan")
for el in ls:
    el.innerHTML = advan(init(el.innerHTML))
    
ls = doc.select(".marksetup")
for el in ls:
    el.innerHTML = setup(init(el.innerHTML))
    
ls = doc.select(".markhead")
for el in ls:
    el.innerHTML = head(init(el.innerHTML))
    
ls = doc.select(".markother")
for el in ls:
    el.innerHTML = other(init(el.innerHTML))
