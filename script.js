var obj = document.getElementsByClassName("clicky");
for (var i = 0; i < obj.length; i++) {
    obj[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.maxHeight){
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    });
}
var factor = 3; /* Scroll Factor */
window.onscroll = function() {bgparallax()};
function bgparallax() {
    document.body.style.backgroundPosition = ((document.body.scrollLeft || window.pageXOffset)/factor)+"px "
                                           + ((document.body.scrollTop || window.pageYOffset)/factor)+"px";
}
