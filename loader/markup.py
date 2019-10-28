from priz_md import *
from browser import document as doc

ls = doc.select(".markall")
for el in ls:
    el.innerHTML = mark(el.innerHTML)

ls = doc.select(".markinit")
for el in ls:
    el.innerHTML = init(el.innerHTML)

ls = doc.select(".markelem")
for el in ls:
    el.innerHTML = init(el.innerHTML)
    el.innerHTML = elem(el.innerHTML)

ls = doc.select(".marklink")
for el in ls:
    el.innerHTML = init(el.innerHTML)
    el.innerHTML = link(el.innerHTML)
    
ls = doc.select(".markbasic")
for el in ls:
    el.innerHTML = init(el.innerHTML)
    el.innerHTML = basic(el.innerHTML)

ls = doc.select(".markadvan")
for el in ls:
    el.innerHTML = init(el.innerHTML)
    el.innerHTML = advan(el.innerHTML)
    
ls = doc.select(".marksetup")
for el in ls:
    el.innerHTML = init(el.innerHTML)
    el.innerHTML = setup(el.innerHTML)
    
ls = doc.select(".markhead")
for el in ls:
    el.innerHTML = init(el.innerHTML)
    el.innerHTML = head(el.innerHTML)
    
ls = doc.select(".markother")
for el in ls:
    el.innerHTML = init(el.innerHTML)
    el.innerHTML = other(el.innerHTML)
