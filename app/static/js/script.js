$(document).ready(function() {

    $('#train, #max_buddies, .training').hide();

    $('#radio_pre input').click(function() {
       $('#train, #max_buddies, .training').show();
    });

    $('#radio_inc input').click(function() {
       $('#train, #max_buddies, .training').hide();
    });

    // check input
    $("#register_button").click(function(){
      $(".error").hide();
      var hasError = false;
      var passwordVal = $("#password").val();
      var confirmPasswordVal = $("#confirm_password").val();
      var emailVal = $("#email").val();
      var nameVal = $("#name").val();
      var surnameVal = $("#surname").val();
      var dobVal = $("#dob").val();
      var choiceVal = $('input[name="status"]:checked').val();  
      var privacy = $('#privacy_cb').is(":checked");
      var choiceTraining = $('input[name="training"]:checked').val();  


      if (passwordVal == '' || passwordVal.length < 8) {
          $("#password").after('<div class="error">Please enter a password with at least 8 characters long.</div>');
          hasError = true;
      } else if (confirmPasswordVal == '') {
          $("#confirm_password").after('<div class="error">Please re-enter your password.</div>');
          hasError = true;
      } else if (passwordVal != confirmPasswordVal ) {
          $("#confirm_password").after('<div class="error">Passwords do not match.</div>');
          hasError = true;
      } else if ( validateEmail(emailVal) == false) {
          $("#email").after('<div class="error">Please enter an email.</div>');
          hasError = true;
      } else if (nameVal == '') {
          $("#name").after('<div class="error">Please enter a name.</div>');
          hasError = true;
      } else if (surnameVal == '') {
          $("#surname").after('<div class="error">Please enter a surname.</div>');
          hasError = true;
      } else if ( validateDate(dobVal)== false) {
          $("#dob").after('<div class="error">Please enter a valid date.</div>');
          hasError = true;
      } else if (privacy === false) {
      	  $("#privacy_cb").after('<div class="error">Please check privacy.</div>');
          hasError = true;
      } else if (choiceVal == null) {
      	  $('input[name="status"]').after('<div class="error">Please pick one.</div>');
          hasError = true;
        } else if (choiceVal == 'p' && choiceTraining == null) {
          $('input[name="training"]').after('<div class="error">Please pick one.</div>');
          hasError = true;
        }
      // else if (choiceVal == 'p' && train == false) {
      // 	  $("#train_cb").after('<div class="error">Please check the box.</div>');
      //     hasError = true;
      // }
      if(hasError == true) {return false;}
		});

});

$(window).load(function(){
  setTimeout(function(){ $('.flashes span').fadeOut() }, 10000);
});

function validateEmail(email) { 
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

function validateDate(date) { 
    // var re = /^(19|20)\d\d[.](0[1-9]|1[012])[.](0[1-9]|[12][0-9]|3[01])$/;  
  var re = /^(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d$/;   
    return re.test(date);
}