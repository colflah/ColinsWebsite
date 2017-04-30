$(function() {
	$("label#email_error").hide();
	$("button#submit_email").click(function () {
		$("label#email_error").hide();
		var email =  $("input#email").val();
		if (email == "Enter Email."|| email == "") {
			$("label#email_error").show();
			$("input#email").focus();
			return false;
		} 
		//alert(email);return false;
		
		$.ajax({
		  type: "POST",
		  url: "/mailinglist",
		  data: 'email='+$("input#email").val(),
		  success: function () {
		  	$('div#email_div').html('<div>Hi</div>');
		    //$('div#email_div').html('<div id="emailSubmitted"></div>');
		    //$("div#emailSubmitted").html('<p class="black"> Email submitted. Thank you!</p>').hide().fadeIn(1500);
	  	  }
		});
	});
});
