from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import TemplateView


# Create your views here.

def index(request):
    title = "Магазин футболок"
    head = "Главная страница"
    context = {
        'title' : title,
        'head': head,
    }
    return render(request, 'head.html', context)

def shop(request):
    return render(request, 'shop.html')

def basket(request):
    return render(request, 'basket.html')