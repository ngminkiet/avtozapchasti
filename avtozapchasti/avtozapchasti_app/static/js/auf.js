$('#auf-button').click(
    function() {
        let email = $('#exampleInputEmail1').val();
        let password = $('#exampleInputPassword1').val();
        let csrf = $('[name=csrfmiddlewaretoken]').val();
        if(!email) {
            alert('Введите адрес почты');
        }

        if(!password) {
            alert('Введите пароль');
        }

        $.ajax({
            url: '/auf/',
            type: 'POST', // отправляет POST-запрос на сервер
            dataType: 'json',
            data: {
                'email' : email,
                'password' : password,
                'csrfmiddlewaretoken' : csrf
            },
            success: function(data) {
                window.location.href = '/';
            },
            error: function(data) {
                alert('Вы не зарегистрированы')
            }   
        });
    }
);