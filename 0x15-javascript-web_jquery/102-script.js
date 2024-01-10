$(document).ready(function () {
	$('INPUT#btn_translate').click(function () {
		const language_code = $('INPUT#language_code').val();
		$.getJSON(`https://www.fourtonfish.com/hellosalut/hello/`,
			function (data) {
			$('DIV#hello').text(data.hello);
		});
	});
});
