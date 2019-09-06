var tap = document.getElementsByClassName("clicky");
for (var i = 0; i < tap.length; i++) {
    tap[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.maxHeight){
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    });
}
window.onscroll = function() {
    var factor = 3;
    document.body.style.backgroundPosition = ((document.body.scrollLeft || window.pageXOffset)/factor)+"px "
                                           + ((document.body.scrollTop || window.pageYOffset)/factor)+"px";
}
