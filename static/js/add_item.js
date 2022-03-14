let uploadedImage = ''

window.onload = function () {
    let imageInput = document.getElementById("upload-image")
    imageInput.addEventListener('change', function () {
        let file = this.files[0];
        let csrftoken = getCookie('csrftoken');
        $.ajaxSetup({ beforeSend: function(xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        })
        let formData = new FormData()
        formData.append("file", file)
        $.ajax({
            url: 'uploadGoodsImage',
            type: 'POST',
            contentType: false,
            processData: false,
            data: formData,
            dataType: 'text',
            success: function(data) {
                let params = JSON.parse(data)
                if (params.success) {
                    $("#goods-image").removeAttr("src").attr("src", "/media/goodsImages/"+params.name);
                    uploadedImage = params.name
                }else {
                    $("#upload-failed-alert").classList.remove("visually-hidden")
                }

            }
        })
    });

}

function getCookie(name) {
    let cookieValue = null;
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

function publishItem() {
    let goodsName = $("#goodsName").attr("value")
    let goodsPrice = $("#goodsPrice").attr("value")
    let goodsCategory = $("#goodsCategory").attr("value")
    let goodsDesc = $("#goodsDesc").attr("value")

    let formData = new FormData()
    formData.append("goodsName", goodsName)
    formData.append("goodsPrice", goodsPrice)
    formData.append("goodsCategory", goodsCategory)
    formData.append("goodsDesc", goodsDesc)

    if (uploadedImage !== '') {
        formData.append("goodsImage", uploadedImage)
    }
    let csrftoken = getCookie('csrftoken');
    $.ajaxSetup({ beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    })
    $.ajax({
        url: 'addItem',
        type: 'POST',
        contentType: false,
        processData: false,
        data: formData,
        dataType: 'text',
        success: function(data) {
            let params = JSON.parse(data)
            if (params.success) {
                location.replace("user/myItems")
            }else {
                alert("Publish error!")
            }

        }
    })
}