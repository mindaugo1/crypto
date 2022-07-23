from django.core.management.base import BaseCommand
from ...strategy import get_moving_average, get_date_range
import subprocess
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pylab as plt


class Command(BaseCommand):

    def handle(self, **options):
        """ A curve is drawn based on the cryptocurrency moving average and the selected date """
        date_range = get_date_range(numdays=10)
        ma50_list = []
        ma200_list = []
        for day in date_range:
            ma = get_moving_average(date=day, numdays=50, crypto="BTC", currency="EUR")
            ma200 = get_moving_average(date=day, numdays=200, crypto="BTC", currency="EUR")
            ma50_list.append(ma)
            ma200_list.append(ma200)

        data_1 = {"day": date_range, "ma50": ma50_list}
        data_2 = {"day": date_range, "ma200": ma200_list}

        plot_1 = pd.DataFrame(data_1)
        plot_2 = pd.DataFrame(data_2)
        print(plot_1)

        df = pd.DataFrame({'ma50': ma50_list,
                           'ma200': ma200_list})

        moving_average_plot = sns.lineplot(data=df)
        moving_average_plot.set(xlabel='date', ylabel='ma')
        plt.gcf().set_size_inches(13, 10)
        plt.grid()


        # sns.set(style='whitegrid', font_scale=0.5, rc={'lines.linewidth': 2})
        # sns.set_context('paper')
        # plottt_1 = sns.lineplot(x='day', y='ma50', data=hi_1, color='red')
        # plottt_2 = sns.lineplot(x='day', y='ma200', data=hi_2, color='blue')
        # plt.xticks(rotation=45)
        # plt.gcf().set_size_inches(13, 10)
        moving_average_plot.figure.savefig('./fadfasdfadsf50.jpg')
