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
			weight: {
			    required:true,
			    number:true
			},
			height:  {
			    required:true,
			    number:true
			},
			weight: {
				required: true,
				weight: true
			}
		},
			messages:{
				spouse: {
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
		    register:{
					  required:"Please enter Medical Instructor Assigned"
				},
				birthDate: {
					required: " Please enter birthdate"
				},
				weight: {
					required: " Please enter your weight",
					number: " Only numbers allowed"
				},
				height: {
					required: " Please enter your height",
					number: " Only numbers allowed"
				},
			}

	});
});
