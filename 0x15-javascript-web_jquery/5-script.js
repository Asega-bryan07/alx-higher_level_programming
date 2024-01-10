$(document).ready(function () {
	$('DIV#add_item').click(function () {
		$('<li>').text('Item').appendTo('UL.my_list');
	});
});
