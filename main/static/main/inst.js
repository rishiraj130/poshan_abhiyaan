$(function(){
	$.validator.setDefaults({
		highlight: function(element){
			$(element)
			.closest('.form-group')
			.addClass('has-error')
		},
		unhighlight: function(element){
			$(element)
			.closest('.form-group')
			.removeClass('has-error')
		}
	});

	$.validate({
		rules:
		{
			birthDate: "required",
      aadhaarNumber:"required",
      phoneNumber:"required",
      weight: {
			    required:true,
			    number:true
			},
			email: {
				required: true,
				email: true
			}
		},
			messages:{
				email: {
				required: true,
				email: true
			}
		},
        image:{
           required: "Please select a Profile Image"
        },
        aadhaarNumber: {
           required: "Please enter Aadhaar Number"
        },
				birthDate: {
					required: " Please enter birthdate"
				},
				email: {
					required: ' Please enter email',
					email: ' Please enter valid email'
				},
				phoneNumber: {
					required: " Please enter your Phone Number",
					number: " Only numbers allowed"
				},
			}

	});
});
