$(document).ready(function () {

	$('input[name=year]').mask('9999');
	$('input[name=date_record]').mask('99/99/9999');
	$('input[name=duration]').mask('99:99');

	$('#add-artist').validate({
		rules: { name: 'required', surname: 'required', country: 'required' }
	});

	$('#add-studio').validate({
		rules: { name: 'required' }
	});

	$('#add-album').validate({
		rules: { album: 'required', style: 'required', year: 'required', artist: 'required', studio: 'required' }
	});

	$('#add-track').validate({
		rules: { track: 'required', album: 'required', style: 'required', date_record: 'required',
				 duration: 'required', artist: 'required', studio: 'required' }
	});

	$('.add-artist').click(function (e) {
		e.preventDefault();
		if (!$('#add-artist').valid())
			return false;
		sendAjax('/artists/add', $('#add-artist').serialize(), function (answer) {
			setResultOfOperation(answer, 'http://localhost:8000/artists/get', 'artist was not added')});
	});

	$('.add-studio').click(function (e) {
		e.preventDefault();
		if (!$('#add-studio').valid())
			return false;
		sendAjax('/studios/add', $('#add-studio').serialize(), function (answer) {
			setResultOfOperation(answer, 'http://localhost:8000/studios/get', 'studio was not added')});
	});

	$('.add-album').click(function (e) {
		e.preventDefault();
		if (!$('#add-album').valid())
			return false;
		sendAjax('/albums/add', $('#add-album').serialize(), function (answer) {
			setResultOfOperation(answer, 'http://localhost:8000/albums/get', 'album was not added')});
	});

	$('.add-track').click(function (e) {
		e.preventDefault();
		if (!$('#add-track').valid())
			return false;
		sendAjax('/tracks/add', $('#add-track').serialize(), function (answer) {
			setResultOfOperation(answer, 'http://localhost:8000/tracks/get', 'track was not added')});
	});

	$('a[href$=fill-db-from-json]').click(function (e) {
		e.preventDefault();
		sendAjax('/fill-db-from-json', '', function (answer) {
			setResultOfOperation(answer, 'http://localhost:8000/artists/get', 'data was not added')});
	});

	$('.update-artist').click(function (e) {
		e.preventDefault();
		addUpdateForm({ form: $('#upd-artist'), id: $(this).parent().parent().attr('class')});
	});

	$('.upd-artist').click(function (e) {
		e.preventDefault();
		sendAjax('/artists/upd', $('#upd-artist').serialize(), function (answer) {
			setResultOfOperation(answer, 'http://localhost:8000/artists/get', 'artist was not updated')});
	});

});

function setResultOfOperation(res, link, message) {
	if (res == 1)
		$(location).attr("href", link);
	else
		alert(message);
}

function sendAjax(link, data, callback) {
	$.ajax({ url: link, type: 'get', data: data, success: callback });
}

function addUpdateForm(params) {
	params.form.children('.id').remove();
	params.form.append('<input class="id" name="id" type="hidden" value="' + params.id + '" />');
	params.form.show();
}