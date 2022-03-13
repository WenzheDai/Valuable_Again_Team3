window.onload = function () {
    let csrftoken = getCookie('csrftoken');
    $.ajaxSetup({ beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    })
}

function bookGoods(id) {
    let formData = new FormData()
    formData.append('id', id)
    $.ajax({
        url: 'bookGoods',
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
                alert("Book error!")
            }

        }
    })
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