
//Add ingredients to list on button click
var button = document.getElementById("add-button");
var input = document.getElementById("ing-input");
var ul = document.querySelector("ul");

button.addEventListener("click", function() {

  var validate= validate_form() 
  if (validate){
    add_checkbox_to_list();
  }
  else
  {
    alert ( "Please fill in the 'Your Name' box." );
  }
  

})

function add_checkbox_to_list(){

  var li = document.createElement("li");  
  li.classList.add("list-group-item");

  //create checkbox item
  var x = document.createElement("input");
      x.setAttribute("type", "checkbox");
      x.setAttribute("class", "form-check-input me-1");
      x.setAttribute("id", "chk");
  li.appendChild(x);
 
  // add input to list  
  var ing_name = input.value;
  var text = document.createTextNode(ing_name);
  li.appendChild(text);
  ul.appendChild(li);
  // Clear your input 
  input.value = "";

  var  btn= document.createElement("button");
  btn.setAttribute("type", "button");
  btn.setAttribute("class", "btn btn-danger remove btn-sm float-end");
  btn.innerHTML = '<i class="bi bi-trash"></i> ';
        //add an event listener for the delete button
  btn.addEventListener("click", function(){
    
    //get the parent of the span (li) 
    let listItem = this.parentNode;
    //get the parent of the list item (ul)
    let list = listItem.parentNode;
    //remove the child from the list         
    list.removeChild(listItem);
  
  });
li.appendChild(btn);
}

document.getElementById('select-all').onclick = function() {
  var checkboxes = document.querySelectorAll('input[type="checkbox"]');
  for (var checkbox of checkboxes) {
      checkbox.checked = this.checked;
  }
}

function validate_form ( )
{
    valid = true;
    var input = document.getElementById("ing-input");
    if ( input.value == "" )
    {
       
        valid = false;
    }

    return valid;
  }
 