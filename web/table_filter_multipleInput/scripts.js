// Please star/follow https://github.com/LennyDuan/Tool if you think this is useful
// Load the script after DOM ready
document.addEventListener('DOMContentLoaded', function() {
  setHeader();
}, false);

// Add head to array
var headers = [];
function setHeader() {
  var table = document.getElementById("myTable");
  var head = table.getElementsByTagName("tr")[0].getElementsByTagName("th");
  for (var j = 0; j < head.length; j++) {
    var val = head[j].innerHTML;
    headers.push(val);
  }
  console.log(headers);
  createInputs();
}

function createInputs() {
  var start = "<tr onClick='showInputs()' style='display:none'>";
  var end = "</tr>";
  var inputs = start;
  for (var i = 0 ; i < headers.length; i++) {
      var row = "<td><input type='text' onkeyup='filterFunction()''" +
      "placeholder='Search: " + headers[i]+ "'></td>";
      inputs += row;
  }
  inputs += end;
}

function filterFunction() {
  // Declare variables
  var filterInput, filter, table, tr, td, i, headIndex;
  // Get input value
  filterInput = document.getElementById("filterInput");
  filter = filterInput.value.toUpperCase();
  // Define table and tr
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  // Get headIndex;
  headIndex = document.getElementById("selectedId").selectedIndex;

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
