$('#reg-button').click(
    function() {
        let email = $('#email').val();
        let password = $('#password').val();
        let firstName = $('#first-name').val();
        let lastName = $('#last-name').val();
        let csrf = $('[name=csrfmiddlewaretoken]').val();

        if(!email) {
            alert('Введите адрес почты');
        }

        if(!password) {
            alert('Введите пароль');
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
                window.location.href = '/';
            },

        });
    }
);