function filterFunction() {
  // Declare variables
  var columnInput, filterInput, filter, table, tr, td, i, columnValue, head, headIndex;
  columInput = document.getElementById("headerInput");
  filterInput = document.getElementById("filterInput");
  filter = filterInput.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");


  columnValue = columInput.value.toUpperCase();
  if(columnValue) {
  head = table.getElementsByTagName("th");
} else {
  headIndex = 0;
}

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[headIndex];
    if (td) {
      if (td.innerHTML.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}
