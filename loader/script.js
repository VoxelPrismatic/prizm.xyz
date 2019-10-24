// VARS
doc = document
win = window
// GET
function gID(elem) { return doc.getElementById(elem); }
function gHTML(elem) { return gID(elem).innerHTML; }
function gPARAM(elem) { return gID(elem).outerHTML; }
function gSTYLE(elem, name) { return gID(elem).style.getPropertyValue(name); }
function gCLASS(clss) { return doc.getElementsByClassName(clss); }
function gTAG (tag) { return doc.getElementsByTagName(tag); }

// EDIT
function eCLASS(elem, name) { gID(elem).classList.toggle(name); }
function eHTML(elem, val) { gID(elem).innerHTML = val; }
function ePARAM(elem, val) { gID(elem).outerHTML = val; }
function eSTYLE(elem, name, val) { gID(elem).style.setProperty(name, val.split(' ')[0], val.split(' ')[1]); }
function eSET(elem, attr, val) { gID(elem).setAttribute(attr, val); }

var tap = gCLASS("clicky");
for (var i = 0; i < tap.length; i++) {
    tap[i].onclick = function() {
        var taq = gCLASS("clicky");
        for (var i = 0; i < taq.length; i++) {
            if (taq[i].id != this.id) {
                taq[i].classList = taq[i].className.replace(/ (active|select)/g, "");
                taq[i].nextElementSibling.style.height = "0px";
            }
        }
        var nxt = this.nextElementSibling;
        eCLASS(this.id, "select");
        if (this.classList.toggle("active"))
            nxt.style.height = `${nxt.scrollHeight + 10}px`
        else
            nxt.style.height = "0px";
    }
}
var parallax = doc.body.style;
win.onscroll = function() {
    parallax.backgroundPosition = 
        `center ${win.pageYOffset/4.0}px`;
}
function chng() {
    var tab = gHTML("labels").split('|');
    for (var i = 0; i < tab.length; i++) {
        gID(tab[i]).onclick = function() {
            var tag = gHTML("labels").split('|');
            for (var i = 0; i < tag.length; i++) {
                gID(tag[i]).className = gID(tag[i]).className.replace(" active", "");
            }
            eHTML("blocky", gHTML("changes_"+this.id));
            this.className += " active"
        }
    }
}

function comm() {
    var tab = document.getElementById("labels").innerHTML.split('|');
    for (var i = 0; i < tab.length; i++) {
        gID(tab[i]).onclick = function() {
            var tag = gHTML("labels").split('|');
            for (var i = 0; i < tag.length; i++) {
                gID(tag[i]).className = gID(tag[i]).className.replace(" active", "");
            }
            eHTML("blocky", gHTML("commands_"+this.id));
            this.className += " active"
        }
    }
}

function markup(itm) {
    itm.innerHTML = window.mark(itm.innerHTML);
}
