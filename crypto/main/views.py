from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from .strategy import get_moving_avarage


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
    list_of_moving_avarage = []
    for date in ["2022-06-01", "2022-06-02", "2022-06-03", "2022-06-04"]:
        ma50 = get_moving_avarage(start_date=date, days=50, currency="EUR", crypto="BTC")
        list_of_moving_avarage.append(ma50)
    context = {'labas': 'labas vakaras', 'vardas': vardas, 'average': list_of_moving_avarage}
    return render(request, 'graph.html', context)
