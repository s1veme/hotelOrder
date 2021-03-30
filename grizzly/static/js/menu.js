console.log('Okey')

function openFunction() {
    document.getElementById("menu").style.width = "300px";
    document.getElementById("menubox").style.marginLeft = "300px";
    document.getElementById("menubox").innerHTML = "";
}

function closeFunction() {
    document.getElementById("menu").style.width = "0px";
    document.getElementById("menubox").style.marginLeft = "0px";
    document.getElementById("menubox").innerHTML = "&#9776;";
}