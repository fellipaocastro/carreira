from datetime import datetime

import matplotlib.pyplot as plt
from matplotlib import ticker
import numpy as np
import pandas as pd
import seaborn as sns


def format_date(date):
    date = str(date)
    return datetime.strptime(date, '%d/%m/%Y') if date != 'nan' else datetime.now()


def format_y_axis(y_param, _pos):
    y_axis = ''

    anos = y_param / 365

    if anos >= 1:
        ano_str = 'anos' if anos >= 2 else 'ano'

        y_axis = f'{anos:.1f} {ano_str}'.replace('.', ',')
    elif y_param > 0:
        meses = int(np.mod(y_param, 365) / 30)

        y_axis = f'{meses} meses'

    return y_axis


if __name__ == '__main__':
    sns.set_style('whitegrid')
    # %matplotlib inline

    carreira = pd.read_csv('carreira/carreira.csv', delimiter=';')
    carreira['entrada'] = carreira['entrada'].apply(format_date)
    carreira['saida'] = carreira['saida'].apply(format_date)
    carreira['dias'] = (carreira['saida'] - carreira['entrada']).dt.days + 1

    carreira['inicio'] = carreira['entrada'].dt.strftime('%m/%Y')

    BGCOLOR = '#fbf0d9'

    fig, ax = plt.subplots(figsize=(10, 5))
    fig.set_facecolor(BGCOLOR)
    ax.set_facecolor(BGCOLOR)

    formatter = ticker.FuncFormatter(format_y_axis)
    ax.yaxis.set_major_formatter(formatter)

    sns.barplot(data=carreira, x='inicio', y='dias', hue='esfera', palette=sns.color_palette(['#a61c00', '#1c4587']),
                ax=ax)

    plt.title('Carreira', fontsize=14)
    plt.xlabel('Início', fontsize=12)
    plt.ylabel('Tempo', fontsize=12)
    plt.legend(fontsize=11)

    for container in ax.containers:
        for rect in container:
            height = rect.get_height()
            x_pos = rect.get_x() + rect.get_width() / 2
            y_pos = height + 20
            text = carreira.iloc[container.index(rect)]['instituicao']
            ax.annotate(text, xy=(x_pos, y_pos), ha='center', fontsize=11)

    plt.savefig('carreira/carreira.png')
    plt.show()