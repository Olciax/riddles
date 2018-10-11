document.addEventListener("DOMContentLoaded", function() {

    $("#hint_button").on('click', function (e) {


        $.get('/points/', function (ret_data) {
            $("#current_points").text(ret_data);

            $("#hint_button").attr('disabled', 'disabled');

        });

    });
    $(document).ready(function(){
        $('[data-toggle="tooltip"]').tooltip();


        })

    (function() {
        var preload = document.getElementById("preload");
        var loading = 0;
        var id = setInterval(frame, 64);

        function frame() {
            if(loading == 100) {
                clearInterval(id);
                window.open("base2.html", "_self");

            }   else{
                loading = loading + 1;
                if(loading == 90) {
                    preload.style.animation = "fadeout 1s ease";
                }
            }
        }
    })



});


