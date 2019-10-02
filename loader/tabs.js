var tab = document.getElementsByClassName("tabby_link");
console.log(tab)
for (var i = 0; i < tab.length; i++) {
    tab[i].onclick = function() {
        var tag = document.getElementsByClassName("tabby_link");
        for (var i = 0; i < tag.length; i++) {
            tag[i].className = tag[i].className.replace(" active", "");
        }
        document.getElementById("blocky").innerHTML = document.getElementById(this.id+"-").innerHTML;
    }
}
