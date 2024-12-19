$(document).ready(function() {
    // Function to calculate age based on date of birth
    $('.dob-input').change(function() {
        var dob = $(this).val();
        if (dob) {
            var today = new Date();
            var birthDate = new Date(dob);
            var age = today.getFullYear() - birthDate.getFullYear();
            var m = today.getMonth() - birthDate.getMonth();
            if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
                age--;
            }
            $('#id_age').val(age);  // Assuming 'id_age' is the ID of your age field in the form
        }
    });
});
