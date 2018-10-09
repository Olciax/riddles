document.addEventListener("DOMContentLoaded", function() {

    $("#hint_button").on('click', function (e) {


        $.get('/points/', function (ret_data) {
            $("#current_points").text(ret_data);

            $("#hint_button").attr('disabled', 'disabled');

        });

    });


});
