
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Lê os dados a partir de um arquivo CSV
    df = pd.read_csv('epa-sea-level.csv')

    # Cria o gráfico de dispersão (scatter plot)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Cria a primeira linha de tendência (regressão linear) usando todos os dados
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Gera uma série de anos de 1880 até 2050 para projetar a linha
    years_extended = pd.Series([i for i in range(1880, 2051)])
    ax.plot(years_extended, res.intercept + res.slope * years_extended, 'r', label='Linha de Ajuste (1880-2050)')

    # Cria uma segunda linha de tendência usando apenas dados a partir de 2000
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_extended_2000 = pd.Series([i for i in range(2000, 2051)])
    ax.plot(years_extended_2000, res_2000.intercept + res_2000.slope * years_extended_2000, 'g', label='Linha de Ajuste (2000-2050)')

    # Configurações visuais do gráfico
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Salva o gráfico como imagem e retorna o eixo (para testes automatizados)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

if __name__ == '__main__':
    draw_plot()

