from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def func_templ(request):
    return render(request, 'func_template.html')

def index(request):
    return render(request, 'index.html')

class Func_class(TemplateView):
    template_name = 'class_template.html'
