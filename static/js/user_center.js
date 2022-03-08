window.onload = function () {
    let avatarInput = document.getElementById("upload-avatar")
    avatarInput.addEventListener('change', function () {
        let file = this.files[0];
        console.log(file)
    })
}

// an input rule just allowed numbers
function keyRules() {
    const k = event.keyCode;
    if ((k <= 57 && k >= 48) || (k <= 105 && k >= 96) || (k == 8)){
        return true;
    } else {
        return false;
    }
}
