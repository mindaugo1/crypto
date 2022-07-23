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
    plt.use('Agg')
    date_range = get_date_range(numdays=10)
    list_of_moving_average = []
    for day in date_range:
        ma = get_moving_average(date=day, numdays=50, crypto="BTC", currency="EUR")
        list_of_moving_average.append(ma)

    moving_graph = sns.lineplot(data=list_of_moving_average, x='date',
                                y='ma', legend='full')
    fig = moving_graph.figure
    graph_file = BytesIO()
    fig.savefig(graph_file, format='png')
    encoded_file = base64.b64encode(graph_file.getvalue())
    context = {'labas': 'labas vakaras', 'vardas': vardas, 'average': list_of_moving_average, 'png_file': encoded_file}
    return render(request, 'graph.html', context)
