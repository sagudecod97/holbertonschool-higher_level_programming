'use strict'
$(document).ready(() => {
    $.ajax({
        url: 'https://swapi.co/api/films/?format=json',
        crossDomain: true
    }).done((data) => {
        let dataResult = data.results;
        dataResult.forEach((title) => $('#list_movies').append(`<li>${title.title}</li>`));
    })
})
