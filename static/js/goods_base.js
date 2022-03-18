function noticeChecked() {
    let csrftoken = getCookie('csrftoken');
    $.ajaxSetup({ beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    })
    $.ajax({
        url: 'notice',
        type: 'POST',
        contentType: false,
        processData: false,
        data: new FormData(),
        dataType: 'text',
        success: function(data) {
            let params = JSON.parse(data)
            if (params.success) {
                location.reload()
            }else {
                alert("Notice error!")
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