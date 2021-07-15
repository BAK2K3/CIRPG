


    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl, {
            html: true,
            container: "body",
            sanitize: false,
            placement: "auto",
            content: function() {
                content_id = $(this).attr("data-content-id")
                return $(content_id).html();
            }
        });
    });

