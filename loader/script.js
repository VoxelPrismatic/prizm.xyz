var tap = document.getElementsByClassName("clicky");
for (var i = 0; i < tap.length; i++) {
    tap[i].onclick = function() {
        var taq = document.getElementsByClassName("clicky");
        for (var i = 0; i < taq.length; i++) {
            if (taq[i].id != this.id) {
                taq[i].classList = taq[i].className.replace(/ (active|select)/g, "");
                taq[i].nextElementSibling.style.height = "0px";
            }
        }
        var nxt = this.nextElementSibling;
        this.classList.toggle("select");
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
    console.log(tab)
    for (var i = 0; i < tab.length; i++) {
        document.getElementById(tab[i]).onclick = function() {
            var tag = document.getElementById("labels").innerHTML.split('|');
            for (var i = 0; i < tag.length; i++) {
                document.getElementById(tag[i]).className = document.getElementById(tag[i]).className.replace(" active", "");
            }
            document.getElementById("blocky").innerHTML = document.getElementById(this.id+"-").innerHTML;
            this.className += " active"
        }
    }
}
window.setTimeout(chng, 2500);
