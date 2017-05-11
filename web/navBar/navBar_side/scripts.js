function openNav() {
  var width = window.innerWidth;
    if(width < 500) {
        document.getElementById("mySidenav").style.width = "100%";
    } else {
      document.getElementById("mySidenav").style.width = "250px";
      document.getElementById("main").style.marginLeft = "200px";
    }

}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}
