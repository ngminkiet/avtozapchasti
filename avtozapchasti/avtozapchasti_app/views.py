from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Item

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

        user = authenticate(request, username=email, password=password)
        print(user)
 
        if user is not None:
            print('auf success')
            login(request, user)
            return JsonResponse({'status' : 'success'})
        else:
            return JsonResponse({'status' : 'error'})
    else:
        return render(request, 'auf.html')

def reg(request):

    # Если приходит POST-запрос
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = email

        # Создаем пользователя
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        login(request, user)
        return JsonResponse({'status' : 'success'})
    return render(request, 'reg.html')    

def logout_view(request):
    logout(request)
    return redirect('index') #перенаправление

def item_template(request, id):
    item = Item.objects.get(id = id) 
    context = {
        'item_title' : item.item_title, 
        'photo' : item.image     
    }
    return render(request, 'item_template.html', context)


        # user = auth5nticate(request, email=email, password=password)
        # if user is n69gin: {username}, password: {password}')
        #     return JsonResponse({'status': 'success', 'message': 'OK'})
        # else:
        #     return JsonResponse({'status': 'error', 'message': 'Неверный логин и пароль'})