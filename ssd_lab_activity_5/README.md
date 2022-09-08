used function for onClick actions 


function myCreateFunction() {
      var table = document.getElementById("studentTable");
      document.getElementById("name").value;
      var row = table.insertRow(1);
      var cell1 = row.insertCell(0);
      var cell2 = row.insertCell(1);
      cell1.innerHTML = document.getElementById("roll").value;
      cell2.innerHTML = document.getElementById("name").value;
      document.getElementById("roll").value="";
      document.getElementById("name").value="";
    }
    
    function myDeleteFunction() {
      document.getElementById("studentTable").deleteRow(1);
    }
