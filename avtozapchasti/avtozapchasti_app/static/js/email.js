$('#submit-button').click(
    function() {
        let email = $('#email').val();
        let submitButton = $('#submit-button');
        const CSRF = $('[name=csrfmiddlewaretoken]').val();
        const emailPattern = /^[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/; // Это регулярное выражение

        if(!emailPattern.test(email)) {
            submitButton.val('Неправильно введён адрес почты');
            submitButton.css('background-color', 'red'); 
            return;          
        }

        $.ajax({
            url: '/email/',
            method: 'POST',
            dataType: 'json',
            data: {
                'email' : email,
                'csrfmiddlewaretoken' : CSRF
            },
            success: function(xhr) {
                if(xhr.responseJSON) {
                    submitButton.val(xhr.responseJSON.message);
                    submitButton.css('background-color', 'green');
                    submitButton.prop('disabled', true);
                }
            },
            error: function(xhr) {
                if(xhr.responseJSON) {
                    submitButton.val(xhr.responseJSON.message);
                    submitButton.css('background-color', 'red');
                }
            }
        })
    }
)