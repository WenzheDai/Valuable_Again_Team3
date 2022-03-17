window.onload = function () {
    if (localStorage.getItem("username") != null && document.getElementsByClassName("welcome-message").length===0){
        document.getElementById("name").value = localStorage.getItem("username")
        document.getElementById("checkRememberName").checked = true
    }
}

function validateForm(){

    let nameInput = document.getElementById("name")
    nameInput.parentElement.classList.add("was-validated")
    let pwInput = document.getElementById("password")
    pwInput.parentElement.classList.add("was-validated")

    if (nameInput.value === '' || pwInput.value === '') {
        return false
    }

    if (document.getElementById("checkRememberName").checked) {
        localStorage.setItem("username", nameInput.value)
    }else {
        localStorage.removeItem("username")
    }

    return true
}