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
var parallax = document.body.style;
window.onscroll = function() {
    parallax.backgroundPosition = 
        `center ${window.pageYOffset/4.0}px`;
}
function chng() {
    var tab = document.getElementById("labels").innerHTML.split('|');
    for (var i = 0; i < tab.length; i++) {
        gID(tab[i]).onclick = function() {
            var tag = gHTML("labels").innerHTML.split('|');
            for (var i = 0; i < tag.length; i++) {
                gID(tag[i]).className = gID(tag[i]).className.replace(" active", "");
            }
            gHTML("blocky", gHTML("changes_"+this.id));
            this.className += " active"
        }
    }
}

function comm() {
    var tab = document.getElementById("labels").innerHTML.split('|');
    for (var i = 0; i < tab.length; i++) {
        gID(tab[i]).onclick = function() {
            var tag = gHTML("labels").innerHTML.split('|');
            for (var i = 0; i < tag.length; i++) {
                gID(tag[i]).className = gID(tag[i]).className.replace(" active", "");
            }
            gHTML("blocky", gHTML("commands_"+this.id));
            this.className += " active"
        }
    }
}
