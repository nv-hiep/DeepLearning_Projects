function delay(callback, ms) {
	var timer = 0;
	return function() {
	  var context = this, args = arguments;
	  clearTimeout(timer);
	  timer = setTimeout(function () {
		callback.apply(context, args);
	  }, ms || 0);
	};
  }


$(document).ready(function() {

	$('#label-span').text( 'Suggestion '.concat( '(', $('input#suggestion').val().trim().split(',').length, ' words)' ))

	$('#form input#input').keyup(delay( function(event) {

		$.ajax({
			// data to Server using POST
			data : {
				text : $('#input').val(),
			},
			type : 'POST',
			url : '/predict'
		})
		.done(function(data) {
			// Data returned from Server, see route(/predict) in app.py
			if (data.error) {
				$('#input').val(data.text);
				$('#error').text(data.error).show();
				$('#success').hide();
			}
			else {
				$('#success').text( 'Seems good...'.concat( '(', data.text.trim().split(" ").length, ' words)' )).show();
				// $('#input').val(data.text);
				$('#error').hide();
				$('input#suggestion').tagsinput('destroy');
				$('input#suggestion').tagsinput();
				$('input#suggestion').val(data.results);
				$('#label-span').text( 'Suggestion '.concat( '(', $('input#suggestion').val().trim().split(',').length, ' words)' ))
			}

		});

		event.preventDefault();

	}, 200)); //ms = 200 ms

});