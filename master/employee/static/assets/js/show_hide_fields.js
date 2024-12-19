$(document).ready(function() {
    // Function to show/hide PF fields based on selection
    $('.pf-applicable').change(function() {
        var selection = $(this).val();
        if (selection === 'yes') {
            $('.pf-date-field, .pf-no-field, .esi-no-field').show();
        } else {
            $('.pf-date-field, .pf-no-field, .esi-no-field').hide();
        }
    });

    // Trigger change event on page load if necessary
    $('.pf-applicable').change();
});
