$(function() {
    $('#btnSummarize').click(function() {
        $.ajax({
            url: '/summarize',
            data: $('form').serialize(),
	    method: 'POST',
            success: function(response) {
            	
            	var list = $('<ul />'); // create UL
				extractResult(list, $.parseJSON(response));   // run function and fill the UL with LI's
               $('#result').html(list)
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    $('#btnLDASummarize').click(function() {
        $.ajax({
            url: '/ldasummarize',
            data: $('form').serialize(),
	    method: 'POST',
            success: function(response) {

            	var list = $('<ul />'); // create UL
				extractResult(list, $.parseJSON(response));   // run function and fill the UL with LI's
               $('#result').html(list)
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
   

	function extractResult(list, result){     
    	jQuery.each(result, function(key, value) {
        // create a LI for each iteration and append to the UL
        $('<label />', {text: key}).appendTo(list);
        	jQuery.each(value, function(key, point) {
        		$('<li />', {text: point}).appendTo(list);});
        $('<br/>').appendTo(list);	
        // $('<li />', {text: value}).appendTo(list);
    });
}
});
