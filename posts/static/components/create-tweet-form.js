$(document).ready(function () {
    // Post Character Count
    $("#id_direct-content").keyup(function () {
        $("#direct-char-count").text($(this).val().length + " / 255 characters");
    });

    $("#id_modal-content").keyup(function () {
        $("#modal-char-count").text($(this).val().length + " / 255 characters");
    });

    $("#id_reply-content").keyup(function () {
        $("#reply-char-count").text($(this).val().length + " / 255 characters");
    });

    // Auto resize text area
    $('.tweet-content').on('input', function () {
        this.style.height = 'auto'; 
        this.style.height = (this.scrollHeight) + 'px'; 
    });

    // Disable & Enable Post Button
    $('#direct-submit-btn').prop('disabled', true);
    $('#modal-submit-btn').prop('disabled', true);
    $('#reply-submid-btn').prop('disabled', true);
    disable_submit("#direct-submit-btn", "#id_direct-content")
    disable_submit("#modal-submit-btn", "#id_modal-content")
    disable_submit("#reply-submit-btn", "#id_reply-content")

    function disable_submit (btn_id, textarea_id) {
        $(textarea_id).on('input', function () {
            if ($(this).val().trim() !== '') {
                $(btn_id).prop('disabled', false);
            } else {
                $(btn_id).prop('disabled', true);
            }
        })
    }
});