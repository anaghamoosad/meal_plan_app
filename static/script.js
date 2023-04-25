
//Add ingredients to list on button click
 
var loader =document.getElementById("loader");
var button1 =document.getElementById("generateplan");

document.getElementById("generateplan").addEventListener("click", function() {

  loader.style.display = "block";

})


function generate() {
  var doc = new jsPDF('l', 'pt');      
  var res = doc.autoTableHtmlToJson(document.getElementById("meal-table"));     
  var header = function(data) {
    doc.setFontSize(25);
    doc.setTextColor(40);
    doc.setFontStyle('normal');
    doc.text("Weekly Meal Plan", data.settings.margin.left, 50);
  };
  var options = {
    beforePageContent: header,
    margin: {
      top: 100
    },     
    theme: 'grid',
    columnStyles: {
        0: {
            
           cellWidth: '80',
            overflow: 'linebreak'
                            
            },
        1: {
          
          cellWidth: '20',
          overflow: 'linebreak'
           
           },
        2: {
           
            cellWidth: '80',
            overflow: 'linebreak'
           
           },
        3: {
             
            cellWidth: '80' ,
            overflow: 'linebreak'
           },
        4   : {
             
            cellWidth: '80',                 
            overflow: 'linebreak'
           },
    },
    rowStyles: {
   
      0: {
        cellWidth: '80',
        rowHeight: '80'
        },
    1: {
      rowHeight: '80'
       },
    2: {
      rowHeight: '80'
       },
    3: {
      rowHeight: '80'
       },
    4   : {
      rowHeight: '80'
       }
    },
   
  };

  doc.autoTable(res.columns, res.data, options);
 

  doc.save("weeklymealplan.pdf");
}