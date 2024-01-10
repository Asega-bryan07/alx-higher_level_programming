$(socument).ready(function () {
	$('DIV#add_item').click(function () {
		$('<li>').text('Item').appendTo('UL.my_list');
	});
	$('DIV#remove_item').click(function () {
		$('UL.my_list li:last-child').remove();
	});
	$('DIV#clear_list').click(function () {
		$('UL.my_list').empty();
	});
});
