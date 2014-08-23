function show_modal_error(title, message) {
	$('#error_modal h4').text(title);
	$('#error_modal p').text(message);
	$('#error_modal').modal({});
}

$(function() {
	// if there are footnotes, make a copy of the Prev/Next nav
	// links so they appear above the footnotes
	var pn = $('.prev_next');
	var footnotes = $('.footnotes');
	pn.clone().insertBefore(footnotes);

	// make paragraphs contianing images figures
	$('#content img').parent('p').addClass('figure');

	// make tables .tables (a bootstrap style)
	$('#content > table').addClass("table")

	// make all images responsive
	$('#content img').addClass('img-responsive');
})