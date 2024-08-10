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
    shop = " Магазин "
    menu_shop = ' Футболки '
    catalog = ['Футболка с начесом', 'Футболка с принтом', 'Футболка обычная']
    context = {
        'shop': shop,
        'menu_shop': menu_shop,
        'catalog':  catalog
    }
    return render(request, 'shop.html', context)

def basket(request):
    return render(request, 'basket.html')