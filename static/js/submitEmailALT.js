$(function() {
	$("label#email_error").hide();
	$("button#submit_email").click(function (event) {
		event.preventDefault();
		$("label#email_error").hide();
		var email =  $("input#email").val();
		if (email == "Enter Email."|| email == "") {
			$("label#email_error").show();
			$("input#email").focus();
			return false;
		} 
		//alert(email);return false;
		payload = 'email='+$("input#email").val();
		$.ajax({
		  type: "POST",
		  url: "/mailinglist",
		  data: payload,
		  success: function () {
		  	//$('div#email_div').empty().html('Hi');
		    $('div#email_div').fadeOut(100, function () {
			$("#email_error").hide();
			$("#submit_email").hide();
			$("div#input_div").empty().html('<div id="emailSubmitted"></div>');
			$("div#email_div").show();
    		        $("div#emailSubmitted").html('<p class="black"> Email submitted. Thank you!</p>').hide().fadeIn(1500);
		    });
	  	  }
		});
	});
});
