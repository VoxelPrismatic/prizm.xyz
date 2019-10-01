var tap = document.getElementsByClassName("clicky");
for (var i = 0; i < tap.length; i++) {
    tap[i].nextElementSibling.style.transition = `height ease ${(content.scrollHeight + 5)/1000}s`;
    tap[i].onclick = function() {
        if (this.classList.toggle("active")) {
            this.nextElementSibling.style.height = `${content.scrollHeight + 5}px`
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
