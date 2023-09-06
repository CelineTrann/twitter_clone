$(document).ready(function () {
    // Open Post Modal
    $("#nav-post-btn").on("click", function () {
        $(".post-modal").show();
        $("#id_modal-content").val("");
        $("#modal-char-count").text("0 / 255 characters");
    })

    // Close Post Modal
    $("#post-modal-close, .post-modal").click(function (event) {
        if (event.target === this) {
            $(".post-modal").hide();
        }
    });

    // Post Character Count
    $("#id_direct-content").keyup(function () {
        $("#direct-char-count").text($(this).val().length + " / 255 characters");
    });

    $("#id_modal-content").keyup(function () {
        $("#modal-char-count").text($(this).val().length + " / 255 characters");
    });

    // Disable & Enable Post Button
    $('.post-btn-submit').prop('disabled', true);
    $('.tweet-content').on('input', function () {
        if ($(this).val().trim() !== '') {
            $('.post-btn-submit').prop('disabled', false);
        } else {
            $('.post-btn-submit').prop('disabled', true);
        }

        // Auto resize text area
        this.style.height = 'auto'; 
        this.style.height = (this.scrollHeight) + 'px'; 
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