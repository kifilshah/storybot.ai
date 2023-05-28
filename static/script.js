$(document).ready(function() {
    let promptHistory = [];

    // Initial check for sendButton
    updateSendButton();

    // Event handler to enable or disable sendButton based on userInput
    $('#userInput').on('input', function() {
        updateSendButton();
    });

    $('#sendButton').click(function(event) {
        event.preventDefault();

        let userInput = $('#userInput').val();
        $('#chatResponseContent').html("<strong>You:</strong> " + userInput);

        // Save the user input to the prompt history
        promptHistory.push(userInput);

        // Display the prompt history
        $('#promptList').empty();
        for (let prompt of promptHistory) {
            $('#promptList').append('<li>' + prompt + '</li>');
        }

        $('#userInput').val('');
        updateSendButton();
        $('#loader').removeClass("d-none");

        // Display the 'Your story is being generated...' message
        $('#chatResponseContent').html("<strong>Bot:</strong> Your story is being generated...");

        $.ajax({
            url: "/ask",
            method: "POST",
            data: { message: promptHistory.join(' ') },
            dataType: "json",
            success: function(data) {
                $('#chatResponseContent').html("<strong>Bot:</strong> " + data.response);
            },
            error: function() {
                $('#chatResponseContent').html("<strong>Bot:</strong> Error");
            },
            complete: function() {
                $('#loader').addClass("d-none");
            }
        });

        return false;
    });

    // Function to update the state of the sendButton
    function updateSendButton() {
        if ($('#userInput').val() === '') {
            $('#sendButton').prop('disabled', true);
        } else {
            $('#sendButton').prop('disabled', false);
        }
    }
});
