let curAvatar = ''
let uploadedAvatar = ''

window.onload = function () {
    curAvatar = $("#big-preview").attr('src')
    let avatarInput = document.getElementById("upload-avatar")
    avatarInput.addEventListener('change', function () {
        let file = this.files[0];
        let csrftoken = getCookie('csrftoken');
        $.ajaxSetup({ beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        })
        let formData = new FormData()
        formData.append("file", file)
        $.ajax({
            url: 'uploadAvatar',
            type: 'POST',
            contentType: false,
            processData: false,
            data: formData,
            dataType: 'text',
            success: function(data) {
                let params = JSON.parse(data)
                if (params.success) {
                    $("#big-preview").removeAttr("src").attr("src", "/media/avatars/"+params.name);
                    $("#sm-preview").removeAttr("src").attr("src", "/media/avatars/"+params.name);
                    uploadedAvatar = params.name
                }else {
                    $("#upload-failed-alert").classList.remove("visually-hidden")
                }

            }
        })
    });

    let myModal = document.getElementById('upload-avatar-modal')
    myModal.addEventListener('hidden.bs.modal', function (event) {
        $("#big-preview").removeAttr("src").attr("src", curAvatar);
        $("#sm-preview").removeAttr("src").attr("src", curAvatar);
        uploadedAvatar = ''
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

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function saveAvatar() {
    if (uploadedAvatar !== '') {
        let formData = new FormData()
    formData.append('avatarName', uploadedAvatar)
    let csrftoken = getCookie('csrftoken');
    $.ajaxSetup({ beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    })
    $.ajax({
        url: 'saveAvatar',
        type: 'POST',
        contentType: false,
        processData: false,
        data: formData,
        dataType: 'text',
        success: function(data) {
            let params = JSON.parse(data)
            if (params.success) {
                location.reload()
            }else {
                $("#upload-failed-alert").classList.remove("visually-hidden")
            }

        }
    })
    }
    location.reload()
}