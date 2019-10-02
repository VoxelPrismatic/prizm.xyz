var tap = document.getElementsByClassName("clicky");
for (var i = 0; i < tap.length; i++) {
    tap[i].onclick = function() {
        this.classList.toggle("select");
        if (this.classList.toggle("active")) {
            this.nextElementSibling.style.height = `${this.nextElementSibling.scrollHeight + 5}px`
        } else {
            this.nextElementSibling.style.height = "0px";
        }
    }
}
var tab = document.getElementsByClassName("tabby_link");
for (var i = 0; i < tab.length; i++) {
    tab[i].onclick = function() {changeLog(this);}
    console.log(tab[i]);
}
var tab = document.getElementsByClassName("tabby_sect");
for (var i = 0; i < tab.length; i++) {
    tab[i].style.display="none";
    console.log(tab[i]);
}

var parallax = document.body.style;
window.onscroll = function() {
    parallax.backgroundPosition = 
        `center ${(window.pageYOffset || document.body.scrollTop)/2.5}px`;
}
function changeLog(itm) {
    nxt = itm.id+"-";
    console.log("Loading changes '"+nxt+"'");
    var sects = document.getElementsByClassName("tabby_sect");
    for (var i = 0; i < sects.length; i++) {
        sects[i].style.display = "none";
    }
    var lnks = document.getElementsByClassName("tabby_link");
    for (var i = 0; i < lnks.length; i++) {
        lnks[i].className = lnks[i].className.replace(" active", "");
    }
    document.getElementById(nxt).style.display = "block";
    itm.className += " active";
    console.log("done");
}
