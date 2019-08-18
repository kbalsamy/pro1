$(function () {


    $("#baggage-type").on("blur", function () {

        $("#add-item").prop('disabled', false);

    });

    $("#add-item").click(function () {

        var bagRows = $("#baggage-type[type='text']").length

        switch (true) {

            case (bagRows == 1):

                if ($("#baggage-type").val().length > 0) {
                    var form = $("#bag-detail").html()
                    $(".form-holder").append(form)

                }

                break;

            case (bagRows > 1):

                console.log("case 2 ")

                if ($("#baggage-type[type='text']").last().val().length > 0) {

                    var form = $("#bag-detail").html()
                    $(".form-holder").append(form)
                }

                break;

            default:

                $("#add-item").prop('disabled', true);
                break;
        }



    });

    $("#remove-item").click(function () {

        $(".form-holder").children("div:last").remove()

    });



    $("#bag-booking").submit(function () {

        var bt = []


                var s = $(".form-val").children("div").find(":input").map(function(){
                   
                    return $(this).val()            
                }).get().join("-")

                bt.push(s) 
        
                $("#baggage-builder").val(bt)
        
                ($("#baggage-builder").val())
        
    });
    
    
    

});



