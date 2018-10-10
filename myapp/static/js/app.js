document.addEventListener("DOMContentLoaded", function() {

    $("#hint_button").on('click', function (e) {


        $.get('/points/', function (ret_data) {
            $("#current_points").text(ret_data);

            $("#hint_button").attr('disabled', 'disabled');

        });

    });
    $(document).ready(function(){
        $('[data-toggle="tooltip"]').tooltip();
        if($('#checkreg').prop("checked")==false){
                alert("Blabla")
            }

        })

    });



});
