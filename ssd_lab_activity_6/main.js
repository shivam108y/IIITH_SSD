var myInput = document.getElementById("pat_check");
var capital = document.getElementById("capital");
var number = document.getElementById("number");

function allowDrop(ev) {
ev.preventDefault();
}

function drag(ev) {
ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
ev.preventDefault();
var data = ev.dataTransfer.getData("text");
ev.target.appendChild(document.getElementById(data));
}

function matchPassword() {  
var pw1 = document.getElementById("svr_pass");  
var pw2 = document.getElementById("conf_pass");  
if(pw1 != pw2)  
{   
    alert("Passwords did not match");  
} else {  
    alert("Password created successfully");  
}  
}  

myInput.onfocus = function() {
    document.getElementById("message").style.display = "block";
}

myInput.onblur = function() {
    document.getElementById("message").style.display = "none";
}

// When the user starts to type something inside the password field
myInput.onkeyup = function() {
    // Validate capital letters
    var upperCaseLetters = /[A-Z]/g;
    if(myInput.value.match(upperCaseLetters)) {
    message.classList.remove("invalid");
    message.classList.add("valid");
    } else {
    message.classList.remove("valid");
    message.classList.add("invalid");
    }

    // Validate numbers
    var numbers = /[0-9]/g;
    if(myInput.value.match(numbers)) {
    message.classList.remove("invalid");
    message.classList.add("valid");
    } else {
    message.classList.remove("valid");
    message.classList.add("invalid");
    }
}