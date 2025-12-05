from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def auf(request):
    return render(request, 'auf.html')