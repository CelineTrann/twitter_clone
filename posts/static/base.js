$(document).ready(function () {
        // Open Post Modal
    $("#nav-post-btn").on("click", function () {
        $(".post-modal").show();
    })

    // Close Post Modal
    $("#post-modal-close, .post-modal").click(function (event) {
        if (event.target === this) {
            $(".post-modal").hide();
        }
    });

    // Post Character Count
    $(".tweet-content").keyup(function () {
        $(".char-count").text($(this).val().length + " / 255 characters");
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
})