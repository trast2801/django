from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def control(username, pass_, pass_ret, age,users):
    info = {}
    if username in users:
        info = "Пользователь уже существует"
        return  info
    elif pass_ != pass_ret:
        info = "Пароли не совпадают"
        return  info
    elif age < 18:
        info = "Вы должны быть старше 18"
        return  info

    info =  f'Приветствуем {username}'
    return  info

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
        str = control(username, pass_, pass_ret, age, users)
        info = {"error": str}
        return render(request, 'registration_page.html',info)
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
            age = int(form.cleaned_data['age'])
            str = control(username, pass_, pass_ret, age, users)
            info = {"error": str}
            return render(request, 'registration_page.html', info)
    else:
        form = ContactForm()
    return render(request,'registration_page.html', {'form': form} )
