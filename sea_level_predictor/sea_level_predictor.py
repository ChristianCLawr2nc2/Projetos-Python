import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Lê os dados do arquivo CSV "epa-sea-level.csv" e armazena em um DataFrame do pandas
    df = pd.read_csv('epa-sea-level.csv')

    # Cria a figura (fig) e o eixo (ax) onde o gráfico será desenhado
    # figsize define o tamanho da figura (10 de largura por 6 de altura)
    fig, ax = plt.subplots(figsize=(10, 6))

    # Cria um gráfico de dispersão (scatter plot) mostrando a relação entre o ano e o nível do mar
    # Cada ponto representa uma medição feita em determinado ano
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Calcula a primeira linha de tendência (regressão linear) com base em todos os dados disponíveis
    # linregress retorna o coeficiente angular (slope), o intercepto e outros dados da regressão
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Cria uma lista de anos de 1880 até 2050 (inclusive) para projetar a tendência até o futuro
    years_extended = pd.Series([i for i in range(1880, 2051)])

    # Plota a linha de tendência com base na equação da reta: y = intercept + slope * x
    # A linha é desenhada em vermelho ('r') e recebe um rótulo para a legenda
    ax.plot(
        years_extended,
        res.intercept + res.slope * years_extended,
        'r',
        label='Linha de Ajuste (1880–2050)'
    )

    # Cria uma segunda análise de regressão, agora considerando apenas os dados a partir do ano 2000
    # Isso permite comparar a tendência recente com a tendência histórica completa
    df_2000 = df[df['Year'] >= 2000]

    # Calcula a nova regressão linear apenas com os dados mais recentes
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])

    # Gera uma nova série de anos (de 2000 até 2050) para a projeção da segunda linha
    years_extended_2000 = pd.Series([i for i in range(2000, 2051)])

    # Plota a nova linha de tendência (em verde) para os dados de 2000 em diante
    ax.plot(
        years_extended_2000,
        res_2000.intercept + res_2000.slope * years_extended_2000,
        'g',
        label='Linha de Ajuste (2000–2050)'
    )

    # Adiciona título e rótulos aos eixos do gráfico
    ax.set_xlabel('Year')                 # Eixo X: Anos
    ax.set_ylabel('Sea Level (inches)')   # Eixo Y: Nível do mar (em polegadas)
    ax.set_title('Rise in Sea Level')     # Título do gráfico

    # Exibe a legenda com as linhas identificadas (vermelha e verde)
    ax.legend()

    # Salva o gráfico como imagem PNG no diretório atual
    plt.savefig('sea_level_plot.png')

    # Retorna o eixo do gráfico (ax) — útil para testes automatizados ou ajustes posteriores
    return plt.gca()


# Bloco principal — executado apenas se o arquivo for rodado diretamente (não importado como módulo)
if __name__ == '__main__':
    # Chama a função para gerar o gráfico
    draw_plot()
