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
    document.body.style.backgroundPosition = 
        "center "+((document.body.scrollTop || window.pageYOffset)/factor)+"px";
}
