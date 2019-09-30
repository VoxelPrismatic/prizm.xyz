var tap = document.getElementsByClassName("clicky");
for (var i = 0; i < tap.length; i++) {
    tap[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        content.style.transition = `${(content.scrollHeight + 5)/1000}s`
        if (content.style.height){
            content.style.height = null;
        } else {
            content.style.height = `${content.scrollHeight + 5}px`;
        }
    });
}
var parallax = document.body.style;
window.onscroll = function() {
    parallax.backgroundPosition = 
        `center ${(window.pageYOffset || document.body.scrollTop)/4}px`;
}
