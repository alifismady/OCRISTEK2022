

function getExpenseAll(){

}

function getExpenseById(){

}

function addExpense(){

}

function updateExpense(){

}

function deleteExpense(){

}

function getIncomeAll(){

}

function getIncomeGetId(){

}

function addIncomeAll(){

}

function updateIncome(){

}

function deleteExpense(){

}

// Document Function
// Get the modal
var mainContainer = document.getElementById("main");

var modalIncome = document.getElementById("modalIncome");

// Get the button that opens the modal
var btnAddIncome = document.getElementById("inc-btn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btnAddIncome.onclick = function() {
  modalIncome.style.display = "block";
  mainContainer.style.display = "none";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modalIncome.style.display = "none";
  mainContainer.style.display = "flex";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modalIncome) {
    modalIncome.style.display = "none";
    mainContainer.style.display = "flex";
  }
}

var modalExpense = document.getElementById("modalExpense");

// Get the button that opens the modal
var btnAddExpense = document.getElementById("exp-btn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close-2")[0];

// When the user clicks on the button, open the modal
btnAddExpense.onclick = function() {
  modalExpense.style.display = "block";
  mainContainer.style.display = "none";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modalExpense.style.display = "none";
  mainContainer.style.display = "flex";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modalExpense) {
    modalExpense.style.display = "none";
    mainContainer.style.display = "flex";
  }
}