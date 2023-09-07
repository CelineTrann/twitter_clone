$(document).ready(function () {
    // Open Post Modal
    $("#nav-post-btn").on("click", function () {
        $(".post-modal").show();
        $("#id_modal-content").val("");
        $("#modal-char-count").text("0 / 255 characters");
        $('#modal-submit-btn').prop('disabled', true);
    })

    // Close Post Modal
    $("#post-modal-close, .post-modal").click(function (event) {
        if (event.target === this) {
            $(".post-modal").hide();
        }
    });

    // Toggle popup
    $("#profile-preview").click(function (e) {
        e.stopPropagation();
        $("#profile-popup").toggleClass("active");
    });

    $("body").click(function () {
        if ($("#profile-popup").hasClass("active")) {
            $("#profile-popup").removeClass("active");
        }
    });
})