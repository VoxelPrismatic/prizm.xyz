function gID(elem) {
    return document.getElementById(elem);
}
function gHTML(elem) {
    return gID(elem).innerHTML;
}
function gSTYLE(elem, name) {}
function gCLASS(elem, name) {
    gID(elem).classList.toggle(name);
}
function gEDIT(elem, val) {
    gID(elem).innerHTML = val;
}
function gST_EDIT(elem, name, val) {}
