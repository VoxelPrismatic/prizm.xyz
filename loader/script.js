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
var parallax = document.body.style;
window.onscroll = function() {
    parallax.backgroundPosition = 
        `center ${(window.pageYOffset || document.body.scrollTop)/2.5}px`;
}
var tab = document.getElementsByName("findme");
console.log(tab)
for (var i = 0; i < tab.length; i++) {
    tab[i].onclick = function() {
        var tag = document.getElementsByName("findme");
        for (var i = 0; i < tag.length; i++) {
            tag[i].className = tag[i].className.replace(" active", "");
        }
        document.getElementById("blocky").innerHTML = document.getElementById(this.id+"-").innerHTML;
        this.className += " active"
    }
}
