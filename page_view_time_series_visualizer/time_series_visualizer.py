import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
from pandas.plotting import register_matplotlib_converters

# Registra os conversores de data do pandas para o matplotlib (evita avisos de compatibilidade)
register_matplotlib_converters()



# Lê o arquivo CSV contendo as visualizações de página do fórum da freeCodeCamp
# - parse_dates=['date']: converte a coluna 'date' para o tipo datetime
# - index_col='date': define a coluna 'date' como índice do DataFrame
df = pd.read_csv('fcc-forum-pageviews.csv',
                 parse_dates=['date'],
                 index_col='date')


# Limpeza dos dados:
# Mantém apenas os valores entre os percentis de 2,5% e 97,5%, removendo outliers (valores extremos)
df = df[(df['value'] >= df['value'].quantile(0.025)) &
        (df['value'] <= df['value'].quantile(0.975))]


# Função 1: Gráfico de linha (tendência temporal)

def draw_line_plot():
    # Cria uma figura e eixos com tamanho 16x6 polegadas
    fig, ax = plt.subplots(figsize=(16, 6))

    # Plota a linha com as visualizações diárias ao longo do tempo
    ax.plot(df.index, df['value'], color='red', linewidth=1)

    # Define título e rótulos dos eixos
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Salva o gráfico como arquivo de imagem
    plt.savefig('line_plot.png')

    # Retorna o objeto da figura para possível uso posterior (exibição ou teste)
    return fig


# Função 2: Gráfico de barras (média mensal por ano)

def draw_bar_plot():
    # Cria uma cópia dos dados originais
    df_bar = df.copy()

    # Cria colunas separadas de ano e mês a partir do índice (que contém datas)
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()


    # Agrupa os dados por ano e mês e calcula a média de visualizações
    # Em seguida, "desempilha" os meses para que cada coluna represente um mês
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()


    # Cria o gráfico de barras a partir do DataFrame agrupado
    fig = df_bar.plot(kind='bar', figsize=(15, 10)).figure


    # Adiciona rótulos e título
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Average Daily Page Views by Month and Year')


    # Ajusta a legenda com os nomes dos meses em ordem
    plt.legend(title='Months',
               labels=['January', 'February', 'March', 'April', 'May', 'June',
                       'July', 'August', 'September', 'October', 'November', 'December'])

    # Salva o gráfico como imagem
    plt.savefig('bar_plot.png')
    return fig


# Função 3: Gráficos de caixa (box plots)
def draw_box_plot():
    # Cria uma cópia dos dados originais
    df_box = df.copy()

    # Reseta o índice para transformar a data em uma coluna normal
    df_box.reset_index(inplace=True)

    # Cria colunas separadas de ano e mês (abreviação do mês)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Cria dois gráficos de caixa lado a lado
    fig, axes = plt.subplots(1, 2, figsize=(20, 8))


    # 1º Gráfico: por ano (tendência anual)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')  # Título
    axes[0].set_xlabel('Year')                      # Eixo X
    axes[0].set_ylabel('Page Views')                # Eixo Y


    # 2º Gráfico: por mês (sazonalidade)
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    sns.boxplot(x='month', y='value', data=df_box, order=month_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')  # Título
    axes[1].set_xlabel('Month')                            # Eixo X
    axes[1].set_ylabel('Page Views')                       # Eixo Y

    # Salva os gráficos como imagem
    plt.savefig('box_plot.png')
    return fig
