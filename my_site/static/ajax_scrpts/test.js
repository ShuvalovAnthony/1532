$("#ajax_test").click(function() {
    $.ajax({
        type: "GET",
        // http://127.0.0.1:8000 - Доменное имя
        url: "http://127.0.0.1:8000/test/",
        data: {
            "username": "test.js[data]",
        },
        dataType: "text",
        cache: false,
        success: function(data) {
            if (data == 'ok'){
                console.log("ok get");
                
            }
            else {
                console.log("error get");
            }
        }
    });
});