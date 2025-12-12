from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def auf(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email, password)
    else:
        return render(request, 'auf.html')