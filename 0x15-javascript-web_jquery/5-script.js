'use strict'
window.addEventListener('load', () => {
    $('#add_item').click(() => {
        $('.my_list').append('<li>Item</li>')
    })
})