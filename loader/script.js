var tap = document.getElementsByClassName("clicky");
for (var i = 0; i < tap.length; i++) {
    var content = this.nextElementSibling;
    tap[i].nextElementSibling.style.transition = `${(content.scrollHeight + 5)/1000}s`;
    tap[i].onclick = function() {
        if (this.classList.toggle("active")) {
            content.style.height = `${content.scrollHeight + 5}px`
        } else {
            content.style.height = "0px";
        }
    }
}
var parallax = document.body.style;
window.onscroll = function() {
    parallax.backgroundPosition = 
        `center ${(window.pageYOffset || document.body.scrollTop)/2.5}px`;
}
