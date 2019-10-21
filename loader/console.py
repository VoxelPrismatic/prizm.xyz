from browser import document as doc, html, window as win, alert
# GET
def gID(elem): return doc[elem]
def gHTML(elem): return gID(elem).innerHTML
def gPARAM(elem): return gID(elem).outerHTML
def gSTYLE(elem, name): return gID(elem).style.getPropertyValue(name)
def gCLASS(clss): return getElementsByClassName(clss)
def gTAG (tag): return getElementsByTagName(tag)

# EDIT
def eCLASS(elem, name): gID(elem).classList.toggle(name)
def eHTML(elem, val): gID(elem).innerHTML = val
def ePARAM(elem, val): gID(elem).outerHTML = val
def eSTYLE(elem, name, val): gID(elem).style.setProperty(name, val.split(' ')[0], val.split(' ')[1])
def eSET(elem, attr, val): gID(elem).setAttribute(attr, val)

# DOCUMENT
def dELEM(typ, *a, **kw): return eval(f"html.{typ.upper()}({', '.join(a)}, {', ',join(key+'='+kw[key] for key in kw)}")

# WINDOW
def wTO(fn, inter): return window.setTimeout(fn, inter)
def wSI(fn, inter): return window.setInterval(fn, inter)
