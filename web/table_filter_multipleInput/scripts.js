// Please star/follow https://github.com/LennyDuan/Tool if you think this is useful
// Load the script after DOM ready
document.addEventListener('DOMContentLoaded', function() {
  insertHeaderFilter();
}, false);

// create an string array of header' values
var headers = [];
function insertHeaderFilter() {
  var table = document.getElementById("myTable");
  var headerRow = table.getElementsByTagName("tr")[0];
  var headerElements = headerRow.getElementsByTagName("th");
  for (var j = 0; j < headerElements.length; j++) {
    var val = headerElements[j].innerHTML;
    headers.push(val.toLowerCase());
  }

  // insert multi-inputs below header
  headerRow.insertAdjacentHTML('afterend', createFilterInputs());
}

// create multi-inputs elements
function createFilterInputs() {
  var inputs = '';
  for (var i = 0 ; i < headers.length; i++) {
      inputs += "<td><input id='" + headers[i] + "_filter' placeholder='Search: " + headers[i]+ "'></td>";
  }
  return "<tr onkeyup='filterFunction()'>" + inputs + "</tr>";
}

function filterFunction() {
  var inputFilterID, filterInput;
  var isSearch = false;
  var tr = document.getElementById("myTable").getElementsByTagName("tr");
  var totalRow = [tr.length];

  // identify the rows which need to be filtered via multi-input.
  for(var columnIndex = 0; columnIndex < headers.length; columnIndex ++) {
    inputFilterID = headers[columnIndex] + '_filter';
    filterInput = document.getElementById(inputFilterID).value.toUpperCase().trim();

    // only iterate the column which has filter input
    if(filterInput) {
      isSearch = true;
      // set true value to the row that need to be filtered
      iterateColumn(tr, filterInput, columnIndex, totalRow);
    }
  }

  // filter table
  filterRows(tr, totalRow, isSearch);
}

// Loop through all table rows, and set true value to the rows that needs to be filtered
function iterateColumn(tr, filterInput, columnIndex, totalRow) {
  var td;
  // Loop through rows for a column that has filter input value
  for (var i = 2; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[columnIndex];
    if (td) {
      // set true value to the row that match the input value
      if (td.innerHTML.toUpperCase().indexOf(filterInput) < 0) {
        totalRow[i] = true;
      }
    }
  }
}

function filterRows(tr, totalRow, isSearch) {
  var rowIndex = 2;
  // filter the rows exclude the header row and filter-input row.
  if(isSearch) {
    for (; rowIndex < tr.length; rowIndex++) {
      // set display feature to 'none' if this row is marked as true value.
      if(totalRow[rowIndex]) {
        tr[rowIndex].style.display = "none";
      } else {
        tr[rowIndex].style.display = "";
      }
    }
  } else {
    // display the whole table if doesn't have input
    for (; rowIndex < tr.length; rowIndex++) {
      tr[rowIndex].style.display = "";
    }
  }
}
