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
               $(window).scrollTop($('#result').offset().top-20)
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
               $(window).scrollTop($('#result').offset().top-20)
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
	
	$('#fbImg').click(function() {
	 	jQuery.get('static/img/facebook.txt', function(data) {
   			$('#inputText').val(data)
//    			$('#length').html("Total words:"+ data.length)
		});
	})
	
	$('#goImg').click(function() {
	 	jQuery.get('static/img/Google.txt', function(data) {
   			$('#inputText').val(data)
//    			$('#length').html("Total words:"+ data.length)
		});
	})
	
	$('#slImg').click(function() {
	 	jQuery.get('static/img/Slack.txt', function(data) {
   			$('#inputText').val(data)
//    			$('#length').html("Total words:"+ data.length)
		});
	})
	
	$('#spImg').click(function() {
	 	jQuery.get('static/img/Spotify.txt', function(data) {
   			$('#inputText').val(data)
//    			$('#length').html("Total words:"+ data.length)
		});
	})
	
	$('#twImg').click(function() {
	 	jQuery.get('static/img/Twitter.txt', function(data) {
   			$('#inputText').val(data)
//    			$('#length').html("Total words:"+ data.length)
		});
	})
});
