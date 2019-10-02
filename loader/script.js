console.log("GRABBING CLICKIES");
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
console.log(tab);
var parallax = document.body.style;
window.onscroll = function() {
    parallax.backgroundPosition = 
        `center ${(window.pageYOffset || document.body.scrollTop)/2.5}px`;
}
var tab = document.getElementsByClassName("tabby_link");
console.log(tab)
for (var i = 0; i < tab.length; i++) {
    tab[i].onclick = function() {
        var tab + document.getElementsByClassName("tabby_link");
        for (var i = 0; i < tab.length; i++) {
            tab[i].className = tab[i].className.replace(" active", "");
        }
        document.getElementById("blocky").innerHTML = document.getElementById(this.id+"-").innerHTML;
    }
}
