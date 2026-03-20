$('#save-button').click(
    function() {
        let email = $('#email').val();
        let password = $('#password').val();
        let birthdate = $('#birthdate').val();
        let firstName = $('#first-name').val();
        let lastName = $('#last-name').val();
        let regButton = $('#save-button');

        const CSRF = $('[name=csrfmiddlewaretoken]').val();

        let userData = {
            'email' : email,
            'password' : password,
            'birthdate' : birthdate,
            'firstName' : firstName,
            'lastName' : lastName,
            'csrfmiddlewaretoken' : CSRF
        }
         $.ajax({
            url: '/account/',
            type: 'POST',
            dataType: 'json',
            data: userData,

            success:
                function(data) {
                    regButton.text('Успешно');
                    regButton.prop('disabled, true');
                    regButton.css({
                        'background-color': '#4CAF50',
                        'color': '#fff',
                    });
                    window.location.href = '/';
                },
         });
    }
); 