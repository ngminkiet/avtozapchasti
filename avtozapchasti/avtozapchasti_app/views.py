from django.shortcuts import render
from django.contrib.auth import login
from django.http import JsonResponse
from django.contrib.auth.models import User

def index(request):
    try:
        context = { 'first_name' : request.user.first_name }
        return render(request, 'index.html', context)         
    except AttributeError as e:
        return render(request, 'index.html')


def auf(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email, password)    
    else:
        return render(request, 'auf.html')

def reg(request):

    # Если приходит POST-запрос
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        # Создаем пользователя
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        login(request, user)
        return JsonResponse({'status' : 'success'})
    return render(request, 'reg.html')
    



    



        # user = authenticate(request, email=email, password=password)
        # if user is not None:
        #     login(request, user)
        #     print(f'login: {username}, password: {password}')
        #     return JsonResponse({'status': 'success', 'message': 'OK'})
        # else:
        #     return JsonResponse({'status': 'error', 'message': 'Неверный логин и пароль'})