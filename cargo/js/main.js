$(function () {

    $(".add-item").click(function () {

        var form = $(".add-form").html()

        $(".form-holder").append(form);

    });

    $(".remove-item").click(function () {


        $(".form-holder").children("div:last").remove();



    });

    $("#baggage-booking").submit(function(){
       
       $("#baggage-option").each(function(){
           
           alert($(this).val())
           
           
           
       });
        
    });




});
