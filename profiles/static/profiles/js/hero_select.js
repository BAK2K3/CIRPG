
$(document).ready(function () {
    
    $(".card").click(function() {
    
        if (!$(this).hasClass("selected-card")) {
            $(".card").removeClass("selected-card");
            $(this).addClass("selected-card");
            $("#HeroForm input").val = $(this).attr("id").slice(0,-4);
            $("#HeroForm button span").html("Create Character");
            $("#HeroForm button").prop("disabled", false);

        }
    });


});