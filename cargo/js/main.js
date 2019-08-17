$(function () {

    $("#add-item").click(function () {
        
        if($("#baggage-type").val().length > 0){
            
            var form = $("#bag-detail").html();

            $(".form-holder").append(form);
        }
        
        

    });

    $("#remove-item").click(function () {

        $(".form-holder").children("div:last").remove()

    });
    
    $("#bag-booking").submit(function(){
        
        var bt = []
            
        $("#baggage-type").each(function(){
           
         var items = $(this).val()
         var length = $("#length").val()
         var width = $("#width").val()
         var height = $("#height").val()
         var weight = $("#weight").val()
         var order= items +"-" + length + "x" + width+"x"+height+"x"+weight
         
         bt.push(order)
            
        });
        
        $("#baggage-type .form-val").each(function(){
            
            bt.push($(this).val())
            
            
        });
      
        
        alert(bt);
        
    });


});
