from priz_md import mark
from browser import document as doc
ls = doc.select(".markme")
for elm in ls:
    elm.innerHTML = mark(elm.innerHTML)
