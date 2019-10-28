from priz_md import *
from browser import document as doc

ls = doc.select(".markall")
for el in ls:
    el.innerHTML = mark(el.innerHTML)

ls = doc.select(".markinit")
for el in ls:
    el.innerHTML = init(el.innerHTML)

ls = doc.select(".marklink")
for el in ls:
    el.innerHTML = link(el.innerHTML)
    
ls = doc.select(".markbasic")
for el in ls:
    el.innerHTML = basic(el.innerHTML)

ls = doc.select(".markadvan")
for el in ls:
    el.innerHTML = advan(el.innerHTML)
    
ls = doc.select(".marksetup")
for el in ls:
    el.innerHTML = setup(el.innerHTML)
    
ls = doc.select(".markhead")
for el in ls:
    el.innerHTML = markhead(el.innerHTML)
    
ls = doc.select(".markother")
for el in ls:
    el.innerHTML = other(el.innerHTML)
