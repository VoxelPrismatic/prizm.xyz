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
function changeLog(itm, date) {
    var sects = document.getElementsByClassName("tabby_sect");
    for (var i = 0; i < tabcontent.length; i++) {
        sects[i].style.display = "none";
    }
    var lnks = document.getElementsByClassName("tabby_link");
    for (var i = 0; i < tablinks.length; i++) {
        lnks[i].className = lnks[i].className.replace(" active", "");
    }
    document.getElementById(date).style.display = "block";
    itm.currentTarget.className += " active";
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
var tab = document.getElementsByClassName("tabby_link content consect");
for (var i = 0; i < tab.length; i++) {
    tab[i].onclick = function() {changeLog(this, tab[i].id+"-")}
}
