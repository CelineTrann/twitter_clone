$(document).ready(function () {
    $('.settings-accordian').click(function () {
        var currPanel = $(this).next();
        currPanel.slideToggle();
        $('.panel').not(currPanel).slideUp();
        if ($('.settings-accordian').not(this).hasClass('active-accordian')) {
            $('.settings-accordian').not(this).removeClass('active-accordian');
        }

        $(this).toggleClass('active-accordian');
        $(this).find('.fa-caret-down').toggleClass('rotate-180');
        $(this).find('.fa-caret-down').toggleClass('rotate-0');
    })
})