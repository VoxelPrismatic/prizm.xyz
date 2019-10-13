// GET
function gID(elem) {
    return document.getElementById(elem);
}
function gHTML(elem) {
    return gID(elem).innerHTML;
}
function gPARAM(elem) {
    return gID(elem).outerHTML;
}
function gSTYLE(elem, name) {
    return gID(elem).style.getPropertyValue(name);
}
// EDIT
function eCLASS(elem, name) {
    gID(elem).classList.toggle(name);
}
function eHTML(elem, val) {
    gID(elem).innerHTML = val;
}
function ePARAM(elem, val) {
    gID(elem).outerHTML = val;
}
function eSTYLE(elem, name, val) {
    gID(elem).style.setProperty(name, val.split(' ')[0], val.split(' ')[1]);
}
// WINDOW
function wTO(fn, inter) {
    return window.setTimeout(fn, inter);
}
function wSI(fn, inter) {
    return window.setInterval(fn, inter);
}
// OTHER
out = console.log
function fns() {
    out(  "AVAILABLE THINGS ]\n"
        + "gID(id: str) --------------------------- Get an element\n"
        + "gHTML(id: str) ------------------------- Get the inner html of an element\n"
        + "gPARAM(id: str) ------------------------ Get the outer html of an element\n"
        + "gSTYLE(id: str, style: str) ------------ Get the style of an element\n"
        + "eCLASS(id: str, name: str) ------------- Toggle the class of an element\n"
        + "eHTML(id: str, content: str) ----------- Edit the inner html of an element\n"
        + "ePARAM(id: str, content: str) ---------- Edit the outer html of an element\n"
        + "eSTYLE(id: str, style: str, val: str) -- Set the style of an element to val\n"
        + "wTO(fn: function, inter: int) ---------- Set the window timeout\n"
        + "wSI(fn: function, inter: int) ---------- Set the window interval\n"
        + "out(vals: any) ------------------------- Shorter version of console.log()\n"
    );
    out(  "EXAMPLES OF THINGS\n"
        + 'gID("elem_id")\n'
        + 'gHTML("elem_id")\n'
        + 'gPARAM("elem_id")\n'
        + 'gSTYLE("elem_id", "style_name")\n'
        + 'ePARAM("elem_id", "style=\'width: auto\'")\n'
        + 'eCLASS("elem_id", "class_name")\n'
        + 'eHTML("elem_id", "content")\n'
        + 'eSTYLE("elem_id", "style_name", "value")\n'
        + 'wTO(function(){out("hi");}, 1200)\n'
        + 'wSI(function(){out("hi");}, 1200)\n'
        + 'out("2", 1, true)\n'
    );
}
out("DEBUG FUNCTIONS LOADED\nTYPE 'fns();' TO SEE NEW FUNCTIONS");
