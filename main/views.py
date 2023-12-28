from django.shortcuts import render
# from .models import Anketa

def index(request):
    # main = Anketa.objects.all()
    # return render(request, 'main/index.html', {'main': main})
    return render(request, 'main/index.html', {'title': 'Главная страница'})

def about(request):
    return render(request, 'main/about.html', {'title': 'Про нас'})