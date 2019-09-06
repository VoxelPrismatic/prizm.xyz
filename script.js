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
    var factor = 3;
    if (window.pageYOffset) {
        var pos = "center "+(window.pageYOffset/factor)+"px";
    } else {
        var pos = "center "+(document.body.scrollTop/factor)+"px";
    }
    document.body.style.backgroundPosition = pos;
}
