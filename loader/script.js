var tap = document.getElementsByClassName("clicky");
for (var i = 0; i < tap.length; i++) {
    tap[i].onclick = function() {
        var taq = document.getElementsByClassName("clicky");
        for (var i = 0; i < taq.length; i++) {
            if (taq[i].id != this.id) {
                taq[i].classList = taq[i].className.replace(" select", "");
                taq[i].classList = taq[i].className.replace(" active", "");
                taq[i].nextElementSibling.style.height = "0px";
            } else {
                this.classList.toggle("select");
                if (this.classList.toggle("active"))
                    this.nextElementSibling.style.height = `${this.nextElementSibling.scrollHeight + 5}px`
                else
                    this.nextElementSibling.style.height = "0px";
            }
        }
    }
}
var parallax = document.body.style;
window.onscroll = function() {
    parallax.backgroundPosition = 
        `center ${(window.pageYOffset || document.body.scrollTop)/2.5}px`;
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
