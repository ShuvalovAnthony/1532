$(document).ready(function () {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    var user_name, user_id;
    user_name = $("#completed_lessons").attr("data-user_name");
    user_id = $("#completed_lessons").attr("data-user_id");
    lesson_id = $("#completed_lessons").attr("data-lesson_id");
    
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            // if not safe, set csrftoken
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/onload_post/",
        data: {
            'user_name': user_name,
            'user_id': user_id,
            'lesson_id': lesson_id,
        },
        dataType: 'text',
        success: function (data) {
            if (data == 'complete'){
                $("#completed_lessons").css('background-color', '#2494ad')
                console.log('complete')
            }
            else if (data == 'uncomplete'){
                console.log('uncomplete')
            }
        },
        error: function () {
            console.log("bad post");
        }
    });
});