function filterFunction() {
  // Declare variables
  var columnInput, filterInput, filter, table, tr, td, i, columnValue, head, headIndex;
  // Get two input value
  columInput = document.getElementById("headerInput");
  filterInput = document.getElementById("filterInput");
  columnValue = columInput.value.toUpperCase();
  filter = filterInput.value.toUpperCase();

  // Define table and tr
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");

  // Find Table Head Index
  if(columnValue) {
    head = table.getElementsByTagName("tr")[0].getElementsByTagName("th");
    for (var j = 0; j < head.length; j++) {
      if(head[j].innerHTML.toUpperCase() == columnValue) {
        headIndex = j;
        break;
      }
    }
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
