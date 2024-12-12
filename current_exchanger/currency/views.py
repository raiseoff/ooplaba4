from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.conf import settings
from currency.models import Currency


def upd_cur():
    try:
        for i in settings.AVAILABLE_CURRENCIES:
            # Проверяем, существует ли запись с таким UID
            currency = Currency.objects.filter(UID=i['UID']).first()
            if currency:
                # Если запись существует, обновляем её
                for key, value in i.items():
                    setattr(currency, key, value)
                currency.save()
            else:
                # Если записи нет, создаём новую
                Currency.objects.create(**i)
    except Exception as e:
        print(e)
        pass


upd_cur()
    

def UserLogin(request):
    context = {
        'title': 'Login',
        'pageTitle': 'Login',
        'btn': 'Login'
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('currency:table')
        else:
            context['err'] = 'Invalid Username or Password'
            return render(request, 'logauth/login.html', context)
    return render(request, 'logauth/login.html', context)

def UserLogout(request):
    logout(request)
    return redirect('currency:login')

def UserRegister(request):
    context = {
        'title': 'Register',
        'pageTitle': 'Register',
        'btn': 'Create'
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            context['err'] = 'Username already exists'
            return render(request, 'logauth/login.html', context)
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('currency:table')
    else:
        return render(request, 'logauth/login.html', context)

def table(request):
    upd_cur()
    if not (request.user.is_authenticated):
        return redirect('currency:login')

    context = {
        'pageTitle': 'Currency Exchange Table',
        'currencies': Currency.objects.all(),
    }
    return render(request, 'currency/table.html', context)


def changer(request):
    if not (request.user.is_authenticated):
        return redirect('currency:login')

    context = {
        'pageTitle': 'Currency Exchange',
        'currencies': Currency.objects.all(),
        'Val': {i.CharCode: {"Value": i.Value, "Nominal": i.Nominal} for i in Currency.objects.all()}
    }
    return render(request, 'currency/changer.html', context)