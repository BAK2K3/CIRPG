
$(document).ready(function () {
    $(".card").click(function() {
        if (!$(this).hasClass("selected-card")) {
            $(".card").removeClass("selected-card");
            $(".card .card-body h5").removeClass("text-decoration-underline")
            $(this).addClass("selected-card");
            $(this).children(".card-body").children("h5").addClass("text-decoration-underline")
            $("#id_user_selection").val($(this).attr("title"));
            $("#HeroForm button span").html("Create Character");
            $("#HeroForm button").prop("disabled", false);
        }
    });
});