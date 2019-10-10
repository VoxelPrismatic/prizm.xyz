function gID(elem) {
    return document.getElementById(elem);
}
function gHTML(elem) {
    return gID(elem).innerHTML;
}
function gSTYLE(elem, name) {
    return gID(elem).style.getPropertyValue(name);
}
function gCLASS(elem, name) {
    gID(elem).classList.toggle(name);
}
function gEDIT(elem, val) {
    gID(elem).innerHTML = val;
}
function gST_EDIT(elem, name, val) {
    gID(elem).style.setProperty(name, val.split(' ')[0], val.split(' ')[1]);
}
