$(document).ready(function () {
    $("body").click(function () {
        if ($(".tweet-popup").hasClass("active-tweet-popup")) {
            $(".tweet-popup").removeClass("active-tweet-popup");
        }
    });
});

function togglePopUp(btn, e) {
    e.stopPropagation();

    // Remove other opened tweet popup
    if ($(".tweet-popup").hasClass("active-tweet-popup")) {
        $(".tweet-popup").removeClass("active-tweet-popup");
    }

    var popup = $(btn).siblings(".tweet-popup");
    popup.toggleClass("active-tweet-popup");
}