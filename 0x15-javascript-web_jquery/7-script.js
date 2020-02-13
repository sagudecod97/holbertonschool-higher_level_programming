'use strict'
window.addEventListener('load', () => {
    $.ajax({
        url: 'https://swapi.co/api/people/5/?format=json',
        crossDomain: true
    }).done((data) => {
        $('#character').text(data.name);
    })
})