$(document).ready(function () {
    $(".following-btn").hover(function () {
        $(this).text("Unfollow");

    }, function () {
        $(this).text("Following");
    });
})
