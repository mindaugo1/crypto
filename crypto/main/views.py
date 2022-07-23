from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from .strategy import get_moving_average, get_date_range
import seaborn as sns
from io import BytesIO
import base64
import matplotlib as plt
from django.shortcuts import render
import pandas as pd
import openpyxl


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
    ma50_list = []
    ma200_list = []
    for day in date_range:
        ma = get_moving_average(date=day, numdays=50, crypto="BTC", currency="EUR")
        ma200 = get_moving_average(date=day, numdays=50, crypto="BTC", currency="EUR")
        ma50_list.append(ma)
        ma200_list.append(ma200)

    data = {"day": date_range, "ma50": ma50_list, "ma200": ma200_list}

    hi = pd.DataFrame(data)
    print(hi)
    sns.set(style='whitegrid')

    plottt = sns.scatterplot(x="day", y="ma50", data=hi)
    plottt.figure.savefig("./fadfasdfadsf.jpg")
