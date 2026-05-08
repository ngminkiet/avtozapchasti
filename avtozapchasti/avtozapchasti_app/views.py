from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Item, UserProfile, EmailCode
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.conf import settings
import random
import threading

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

def send_email_code_async(email, code):
    send_mail(
        'Автозапчасти: код подтверждения',
        f'Ваш код подтверждения: {code}',
        '',
        [email],
        fail_silently=False,
    )

def reg(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        birthdate = request.POST.get('birthdate')

        user = User.objects.create_user(
            username = email, 
            email = email, 
            password = password, 
            first_name = first_name, 
            last_name = last_name,
            is_active = False
        )

        UserProfile.objects.create(
            user = user, 
            birthdate = birthdate
        )

        code = str(random.randint(100000, 999999))

        EmailCode.objects.create(
            user = user,
            code = code
        )

        # send_mail(
        #     'Продукты 24/7: код подтверждения',
        #     f'Ваш код подтверждения: {code}',
        #     'edsuyargulov@yandex.ru',
        #     [email],
        #     fail_silently=False,
        # )

        threading.Thread(
            target=send_email_code_async,
            args=(email, code)
        ).start()        

        request.session['pending_user_id'] = user.id
        return JsonResponse({
            'status': 'success',
            'redirect': '/confirm/'
        })

    if request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request, 'reg.html')  

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index') #перенаправление

def item_template(request, id):
    item = Item.objects.get(id = id) 
    context = {
        'item': item
    }
    return render(request, 'item_template.html', context)

def items_list(request, spare_parts_type):
    spare_parts_name = ''

    if spare_parts_type == 'all':
        items = Item.objects.all()
        spare_parts_name ='Всё'
    else:
        items = Item.objects.filter(spare_parts_type = spare_parts_type)

        spare_parts_types = Item.spare_parts_types

        for ft in spare_parts_types:
            if ft[0] == spare_parts_type:
                spare_parts_name = ft[1]
                break

    context = {
        'items_list' : items,
        'spare_parts_type' : spare_parts_name,
    }

    if request.user.is_authenticated:
        context['username'] = request.user.username

    return render(request, 'catalog.html', context)

def good_template(request, id):
    try:
        item = Item.objects.get(id = id) # конструктор класса
    except ObjectDoesNotExist:
        return render(request, '404.html')

    context = { 
        'item' : item
    }

    if request.user.is_authenticated:
        context['username'] = request.user.username

    return render(request, 'item-template.html', context)

def account(request):

    print(request.user.id)
    context = {
        'username' : request.user.username,
        'first_name' : request.user.first_name,
        'last_name' : request.user.last_name,
        'email' : request.user.email,
    }
    return render(request, 'account.html', context)

def email(request):
    if request.method == 'POST' and request.POST.get('email'):
        
        try:
            email = request.POST.get('email')
            validate_email(email)
            print('Получилось взять имейл: ', email)
        except ValidationError:
            return JsonResponse({'status': 'error', 'message' : 'Неправильно ввёден адрес почты'}, status=400)

def confirm(request):
    if request.method == 'POST':
        code = request.POST.get('email-code')
        user_id = request.session.get('pending_user_id')

        if user_id:
            try:
                user = User.objects.get(id = user_id)
                email_code = EmailCode.objects.get(user = user, code = code)

                if email_code.code == code:
                    if not email_code.is_expired():
                        user.is_active = True
                        user.save()
                        email_code.delete()
                        login(request, user)
                        return JsonResponse({'status' : 'success', 'redirect' : '/account/'})
                    else:
                        return JsonResponse({'status': 'error', 'message': 'Срок действия кода истек'}, status=400)
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Неверный код'}, status=400)

    return render(request, 'confirm.html')
        # send_mail(
        #     "Проверка из Django",
        #     "Привет из Django!",
        #     'edsuyargulov@yandex.ru',
        #     [str(email)],
        #     fail_silently=False,return JsonResponse({'status': 'success', 'message' : 'Отправлено'})
        # )

        
    return JsonResponse({'status' : 'error', 'message' : 'Метод не разрешён. Только POST.'}, status=405)

        # user = auth5nticate(request, email=email, password=password)
        # if user is n69gin: {username}, password: {password}')
        #     return JsonResponse({'status': 'success', 'message': 'OK'})
        # else:
        #     return JsonResponse({'status': 'error', 'message': 'Неверный логин и пароль'})