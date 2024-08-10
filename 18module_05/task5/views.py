from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def sign_up_by_html(request):
    users=["первый","второй", "третий"]
    info ={}
    if request.method == 'POST':
        username = request.POST.get('username')
        pass_ = request.POST.get('pass_')
        pass_ret = request.POST.get('pass_ret')
        age = int(request.POST.get('age'))
        if username in users:
            info = {"error": "Пользователь уже существует"}
            return HttpResponse(f'{info}!')
        elif pass_ != pass_ret:
            info = {"error": "Пароли не совпадают"}
            return HttpResponse(f'{info}!')
        elif age < 18:
            info = {"error": "Вы должны быть старше 18"}
            return HttpResponse(f'{info}!')
        return HttpResponse(f'Приветствуем {username}')
    info = {}
    return render(request, 'registration_page.html', info)


from .forms import ContactForm
def sign_up_by_django(request):
    users = ["первый", "второй", "третий"]
    info = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pass_ = form.cleaned_data['pass_']
            pass_ret = form.cleaned_data['pass_ret']
            age = form.cleaned_data['age']
        if username in users:
            info = {"error": "Пользователь уже существует"}
            return HttpResponse(f'{info}!')
        elif pass_ != pass_ret:
            info = {"error": "Пароли не совпадают"}
            return HttpResponse(f'{info}!')
        elif int(age) < 18:
            info = {"error": "Вы должны быть старше 18"}
            return HttpResponse(f'{info}!')
        return HttpResponse(f'Приветствуем {username}')
    else:
        form = ContactForm()
    return render(request,'registration_page.html', {'form': form} )
