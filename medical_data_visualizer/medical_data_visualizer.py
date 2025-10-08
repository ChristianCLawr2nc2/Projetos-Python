# Importação das bibliotecas necessárias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Lê o arquivo CSV contendo dados médicos e armazena em um DataFrame chamado df
df = pd.read_csv('medical_examination.csv')


# 2. Cálculo do IMC e criação da coluna 'overweight'

# Converte altura de centímetros para metros
df['height_m'] = df['height'] / 100


# Calcula o IMC (Índice de Massa Corporal): peso / (altura²)
df['bmi'] = df['weight'] / (df['height_m'] ** 2)


# Cria uma nova coluna 'overweight':
# - 1 se o IMC for maior que 25 (acima do peso)
# - 0 caso contrário (peso normal ou abaixo)
df['overweight'] = (df['bmi'] > 25).astype(int)


# 3. Normalização dos dados

# Objetivo: padronizar os dados para que 0 = bom e 1 = ruim
# Para 'cholesterol' e 'gluc':
# - Se o valor for 1 (normal), vira 0
# - Se o valor for maior que 1 (acima do normal), vira 1
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


# FUNÇÃO 1: Gráfico categórico (cat plot)

def draw_cat_plot():
    # 5. Reorganizar os dados em formato “longo” (long format)
    # pd.melt transforma várias colunas em pares (variável, valor)
    # Aqui analisamos 6 variáveis de estilo de vida/saúde por paciente
    df_cat = pd.melt(df, 
                     id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6. Agrupar os dados e contar quantos casos existem para cada combinação
    # (cardio, variável, valor)
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')


    # 7. Criar gráfico de barras categórico
    # - x: variável (coluna analisada)
    # - y: total (quantidade)
    # - hue: separação entre valor 0 e 1
    # - col: divide os gráficos entre pessoas com e sem problema cardíaco (cardio)
    fig = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    ).fig

    # 8. Salva o gráfico gerado como imagem
    fig.savefig('catplot.png')
    return fig


# FUNÇÃO 2: Mapa de calor (heat map)

def draw_heat_map():
    # 11. Limpeza dos dados
    # Remove dados incorretos ou extremos:
    # - Pressão diastólica (ap_lo) não pode ser maior que a sistólica (ap_hi)
    # - Altura e peso devem estar dentro do intervalo entre os percentis 2.5% e 97.5%
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Calcula a matriz de correlação (mostra a relação entre as variáveis numéricas)
    corr = df_heat.corr(numeric_only=True)

    # 13. Cria uma máscara para esconder o triângulo superior da matriz (reduz redundância visual)
    mask = np.triu(corr)

    # 14. Define o tamanho da figura
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15. Cria o mapa de calor com anotações dos valores de correlação
    sns.heatmap(
        corr,
        linewidths=1,        # Linhas divisórias entre as células
        annot=True,          # Mostra o valor de correlação dentro de cada célula
        fmt='.1f',           # Formato numérico com uma casa decimal
        mask=mask,           # Aplica a máscara criada
        square=True,         # Mantém as células quadradas
        center=0,            # Centraliza o gradiente de cor no 0
        vmin=-0.5, vmax=0.5, # Define os limites do gradiente de cor
        cbar_kws={'shrink': 0.44}  # Ajusta o tamanho da barra de cores
    )

    # 16. Salva o gráfico como imagem
    fig.savefig('heatmap.png')
    return fig
