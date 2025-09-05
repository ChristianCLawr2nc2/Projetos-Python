import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Importar os dados de medical_examination.csv e atribuí-los à variável df.
df = pd.read_csv('medical_examination.csv')

# 2. Adicionar uma coluna 'overweight' aos dados.
# Para determinar se uma pessoa está acima do peso, primeiro calcule seu IMC dividindo seu peso em quilogramas pelo quadrado de sua altura em metros.
# Se esse valor for > 25, a pessoa está acima do peso. Use o valor 0 para NÃO acima do peso e o valor 1 para acima do peso.
df['height_m'] = df['height'] / 100
df['bmi'] = df['weight'] / (df['height_m'] ** 2)
df['overweight'] = (df['bmi'] > 25).astype(int)

# 3. Normalizar os dados, fazendo com que 0 seja sempre bom e 1 seja sempre ruim.
# Se o valor de 'cholesterol' ou 'gluc' for 1, defina o valor como 0. Se o valor for maior que 1, defina o valor como 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


def draw_cat_plot():
    # 5. Criar um DataFrame para o gráfico de categorias usando pd.melt com valores de 'cholesterol', 'gluc', 'smoke', 'alco', 'active' e 'overweight' na variável df_cat.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Agrupar e reformatar os dados em df_cat para dividi-los por 'cardio'. Mostrar as contagens de cada recurso.
    # Você terá que renomear uma das colunas para que o catplot funcione corretamente.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7. Converter os dados para o formato 'long' e criar um gráfico que mostre as contagens de valores dos recursos categóricos usando o método fornecido pela importação da biblioteca seaborn: sns.catplot().
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig

    # 8. Obter a figura para a saída e armazená-la na variável fig.
    # (Já feito na linha acima)

    # 9. Não modificar as próximas duas linhas.
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # 11. Limpar os dados na variável df_heat filtrando os seguintes segmentos de pacientes que representam dados incorretos:
    # - pressão diastólica é maior que a sistólica (Manter os dados corretos com (df['ap_lo'] <= df['ap_hi']))
    # - altura é menor que o percentil 2.5 (Manter os dados corretos com (df['height'] >= df['height'].quantile(0.025)))
    # - altura é maior que o percentil 97.5
    # - peso é menor que o percentil 2.5
    # - peso é maior que o percentil 97.5
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Calcular a matriz de correlação e armazená-la na variável corr.
    corr = df_heat.corr(numeric_only=True)

    # 13. Gerar uma máscara para o triângulo superior e armazená-la na variável mask.
    mask = np.triu(corr)

    # 14. Configurar a figura do matplotlib.
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15. Plotar a matriz de correlação usando o método fornecido pela importação da biblioteca seaborn: sns.heatmap().
    sns.heatmap(corr, linewidths=1, annot=True, fmt='.1f', mask=mask, square=True, center=0, vmin=-0.5, vmax=0.5, cbar_kws={'shrink': 0.44})

    # 16. Não modificar as próximas duas linhas.
    fig.savefig('heatmap.png')
    return fig


