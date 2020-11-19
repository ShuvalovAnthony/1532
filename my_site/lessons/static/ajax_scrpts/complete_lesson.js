$("#completed_lessons").click(function () {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    var user_name, user_id;
    user_name = $(this).attr("data-user_name");
    user_id = $(this).attr("data-user_id");
    lesson_id = $(this).attr("data-lesson_id");
    
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
        url: "http://127.0.0.1:8000/post/",
        data: {
            'user_name': user_name,
            'user_id': user_id,
            'lesson_id': lesson_id,
        },
        dataType: 'text',
        success: function (data) {
            if (data == 'complete'){
                $("#completed_lessons").css('background-color', '#FF0000')
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