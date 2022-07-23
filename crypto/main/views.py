from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from .strategy import get_moving_avarage, get_date_range


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def graph_view(request, vardas):
    date_range = get_date_range(numdays=10)
    list_of_moving_avarage = []
    for day in date_range:
        ma = get_moving_avarage(date=day, numdays=50, crypto="BTC", currency="EUR")
        list_of_moving_avarage.append(ma) 

    context = {'labas': 'labas vakaras', 'vardas': vardas, 'average': list_of_moving_avarage}
    return render(request, 'graph.html', context)
