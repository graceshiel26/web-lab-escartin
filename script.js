$(document).ready(function() {
    $('#user-form').on('submit', function(event) {
        event.preventDefault();

        const userInput = $('#user_input').val();

        $.ajax({
            url: '/',
            type: 'POST',
            data: {
                user_input: userInput
            },
            success: function(response) {
                $('#user-input-display').text(userInput);
                $('#user-output').show();
                $('#user_input').val('');
            },
            error: function() {
                alert('Error processing the form.');
            }
        });
    });
});