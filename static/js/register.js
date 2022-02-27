
function validateForm(){

    let nameInput = document.getElementById("name")
    let emailInput = document.getElementById("email")
    let pwInput = document.getElementById("password")
    let pwInput2 = document.getElementById("confirm-password")

    nameInput.parentElement.classList.add("was-validated")
    emailInput.parentElement.classList.add("was-validated")
    pwInput.parentElement.classList.add("was-validated")
    pwInput2.parentElement.classList.add("was-validated")

    if (!checkEmail(emailInput.value)) {
        emailInput.classList.add("is-invalid")
        emailInput.parentElement.classList.remove("was-validated")
    }else {
        emailInput.classList.remove("is-invalid")
    }
    if (pwInput2.value !== pwInput.value) {
        pwInput2.classList.add("is-invalid")
        pwInput2.parentElement.classList.remove("was-validated")
    }else {
        pwInput2.classList.remove("is-invalid")
    }

    if (nameInput.value === '' || emailInput.value === '' || !checkEmail(emailInput.value) ||
        pwInput.value === '' || pwInput2.value !== pwInput.value) {
        return false
    }

    return true
}

function checkEmail(emailInputValue){
　　let myReg=/^[a-zA-Z0-9_-]+@([a-zA-Z0-9]+\.)+(com|cn|net|org)$/;

　　return myReg.test(emailInputValue)
}