$(document).ready(function () {

    $(".post-text").on('keydown paste', function (event) {
        var cntMaxLength = parseInt($(this).attr('maxlength'));
        
        const isValidShortcut = (event.ctrlKey && event.keyCode != 86 );
        const isValidKeyCode = [8, 16, 17, 37, 38, 39, 40, 46].includes(event.keyCode);

        var length = $(this).text().length;
    
        if ($(this).text().length >= cntMaxLength && !isValidKeyCode && !isValidShortcut) {
            event.preventDefault();
        } else if (!isValidKeyCode && !isValidShortcut) {
            length++;
        } else if ((event.keyCode == 8 || event.keyCode === 46) & length > 0) {
            length--;
        }

        $("#char-count").text(`${length} / ${cntMaxLength} characters`);
    });
})
