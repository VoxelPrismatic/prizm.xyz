var tap = document.getElementsByClassName("clicky");
for (var i = 0; i < tap.length; i++) {
    tap[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.height){
            content.style.height = null;
        } else {
            content.style.height = content.scrollHeight + "px";
        }
    });
}
window.onscroll = function() {
    document.body.style.backgroundPosition = 
        "center "+((window.pageYOffset || document.body.scrollTop)/3)+"px";
}
