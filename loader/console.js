// VAR
doc = document;
win = window;
// GET
function gID(elem) { return document.getElementById(elem); }
function gHTML(elem) { return gID(elem).innerHTML; }
function gPARAM(elem) { return gID(elem).outerHTML; }
function gSTYLE(elem, name) { return gID(elem).style.getPropertyValue(name); }
function gCLASS(clss) { return document.getElementsByClassName(clss); }
function gTAG (tag) { return document.getElementsByTagName(tag); }

// EDIT
function eCLASS(elem, name) { gID(elem).classList.toggle(name); }
function eHTML(elem, val) { gID(elem).innerHTML = val; }
function ePARAM(elem, val) { gID(elem).outerHTML = val; }
function eSTYLE(elem, name, val) { gID(elem).style.setProperty(name, val.split(' ')[0], val.split(' ')[1]); }
function eSET(elem, attr, val) { gID(elem).setAttribute(attr, val); }

// DOCUMENT
//function dELEM(

// WINDOW
function wTO(fn, inter) { return window.setTimeout(fn, inter); }
function wSI(fn, inter) { return window.setInterval(fn, inter); }

// OTHER
out = console.log
function fns() {
    out(`AVAILABLE THINGS ]
gID(id: str)
    Get an element
    gID("elem_id")

gHTML(id: str)
    Get the inner html of an element
    gHTML("elem_id")

gPARAM(id: str) 
    Get the outer html of an element
    gPARAM("elem_id")

gSTYLE(id: str, style: str) 
    Get the style of an element 
    gSTYLE("elem_id", "style_name")

gCLASS(name: str)
    Get all elements with class "name"
    gCLASS("tabby")

gTAG (name: str)
    Get all elements witha a tag
    gTAG("div")

eCLASS(id: str, name: str) 
    Toggle the class of an element
    eCLASS("elem_id", "class_name")

eSET(id: str, attribute: any, value: any)
    Set an attribute of an element
    eSET("elem_id", "attribute_name", "attribute_value")

eHTML(id: str, content: str) 
    Edit the inner html of an element
    eHTML("elem_id", "content")

ePARAM(id: str, content: str) 
    Edit the outer html of an element
    ePARAM("elem_id", "style=\'style_name: style_value\'")

eSTYLE(id: str, style: str, val: str) 
    Set the style of an element to val
    eSTYLE("elem_id", "style_name", "style_value")

wTO(fn: function, inter: int) 
    Set the window timeout
    wTO(function(){out("hi");}, 1200)

wSI(fn: function, inter: int) 
    Set the window interval
    wSI(function(){out("hi");}, 1200)

out(vals: any) 
    Shorter version of console.log()
    out("2", 1, true)
    `);
}
out("QUICKER FUNCTIONS LOADED\nTYPE 'fns();' TO SEE NEW FUNCTIONS");
out("BRYTHON VERSION ] "+window.__BRYTHON__.__MAGIC__)
