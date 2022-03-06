window.onload = function () {
    let avatarInput = document.getElementById("upload-avatar")
    avatarInput.addEventListener('change', function () {
        let file = this.files[0];
        console.log(file)
    })
}