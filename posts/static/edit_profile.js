$(document).ready(function () {
    // Custom Button click input buttons
    $('#add-cover-pic').click(function () {
        $('#id_cover_picture').click();
    });

    $('#add-profile-pic').click(function () {
        $('#id_profile_picture').click();
    });

    // Preview Image Chosen
    $('#id_cover_picture').on('change', function (e) {
        $('#cover-banner').attr('src', URL.createObjectURL(e.target.files[0]));
        $('#cover-banner').css('background-color', 'var(--twitter-blue)');
    });

    $('#id_profile_picture').on('change', function (e) {
        $('.overlap-banner').attr('src', URL.createObjectURL(e.target.files[0]));
    });
});