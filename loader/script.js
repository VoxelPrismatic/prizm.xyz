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
