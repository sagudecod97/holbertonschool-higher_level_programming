'use strict'
window.addEventListener('load', () => {
    $('#toggle_header').click(() => {
        if ($('header').hasClass('green')) {
            $('header').toggleClass('red');
        } else if ($('header').hasClass('red')) {
            $('header').toggleClass('green ');
        }
    })
})