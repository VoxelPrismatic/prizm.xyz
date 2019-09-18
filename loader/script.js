var tap = document.getElementsByClassName("clicky");
for (var i = 0; i < tap.length; i++) {
    tap[i].addEventListener("click", function() {
        var clicky = document.getElementsByClassName("clicky");
        for (var j = 0; j < clicky.length; j++) {
            if (clicky[j].id != this.id) {
                clicky[j].classList.toggle("active", clicky[j].style.height != null);
                var ct2 = clicky[j].nextElementSibling;
                if (ct2.style.height){
                    ct2.style.height = null;
                }
            }
        }
        this.classList.toggle("active")
        var content = this.nextElementSibling;
        if (content.style.height){
            content.style.height = null;
        } else {
            content.style.height = (content.scrollHeight + 5) + "px";
        }
    });
}
var parallax = document.body.style;
window.onscroll = function() {
    parallax.backgroundPosition = 
        "center "+((window.pageYOffset || document.body.scrollTop)/3)+"px";
}
