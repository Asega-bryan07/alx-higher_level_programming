$(document).ready(function () {
        $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=fr`,
                function(data) {
                $('DIV#character').text(data.hello);
        });
});
