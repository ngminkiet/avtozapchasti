$('#reg-button').click(
    function() {
        let email = $('#email').val();
        let password = $('#password').val();
        let birthdate = $('#birthdate').val();
        let firstName = $('#first-name').val();
        let lastName = $('#last-name').val();
        let regButton = $('#reg-button');

        regButton.prop('disabled', true);
        regButton.prop('hidden', true);
        $('.reg').append(`
            <div id="reg-spinner" class="spinner-border mt-2" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
        `)

        const CSRF = $('[name=csrfmiddlewaretoken]').val();
        
        if(!email) {
            alert('Введите адрес электронной почты!');
        }

        if(!password) {
            alert('Введите пароль!');
        }

        let userData = {
            'email' : email,
            'password' : password,
            'birthdate' : birthdate,
            'firstName' : firstName,
            'lastName' : lastName,
            'csrfmiddlewaretoken': CSRF
        }
    
        $.ajax({
            url: '/reg/',
            type: 'POST', // отправляем POST-запрос на сервер
            dataType: 'json',
            data: {
                'email' : email,
                'password' : password,
                'first_name' : firstName,
                'last_name' : lastName,
                'csrfmiddlewaretoken': csrf
            },
            
            success: function(data) {
                window.location.href = 'data.redirect';
            },
            error: function(xhr) {
                if(xhr.responseJSON) {
                    $('#reg-spinner').remove();
                    regButton.val(xhr.responseJSON.message);
                    regButton.css('background-color', 'red');
                }
            }    
        });
    }
);