$(document).ready(function () {
    $("#nav-post-btn").on("click", function () {
        $(".post-modal").show();
    })

    $("#post-modal-close, .post-modal").click(function (event) {
        if (event.target === this) {
            $(".post-modal").hide();
        }
    });
})