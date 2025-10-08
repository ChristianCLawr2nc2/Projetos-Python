import pandas as pd

def calculate_demographic_data(filepath):


    # Lê o dataset a partir do arquivo CSV indicado no caminho "filepath"
    df = pd.read_csv(filepath)


    # 1. Conta quantas pessoas há de cada raça no conjunto de dados
    # A função value_counts() conta quantas vezes cada valor aparece na coluna "race"
    race_count = df['race'].value_counts()


    # 2. Calcula a média de idade dos homens
    # Filtra apenas as linhas em que o sexo é "Male" e calcula a média da coluna "age"
    # A função round(..., 1) arredonda o resultado para uma casa decimal
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)


    # 3. Calcula a porcentagem de pessoas com ensino superior (Bacharelado)
    # Conta quantas linhas têm "Bachelors" na coluna "education"
    # Divide pelo total de registros e multiplica por 100 para obter a porcentagem
    percentage_bachelors = round(df.loc[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100, 1)


    # 4. Calcula a porcentagem de pessoas com ensino avançado (Bacharelado, Mestrado ou Doutorado) que ganham mais de 50K
    # Usa isin() para filtrar apenas as pessoas com esses níveis de educação
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = round(
        advanced_education.loc[advanced_education['salary'] == '>50K'].shape[0] / advanced_education.shape[0] * 100, 1
    )


    # 5. Calcula a porcentagem de pessoas sem ensino avançado que ganham mais de 50K
    # O símbolo ~ inverte o filtro, pegando quem NÃO tem educação avançada
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = round(
        lower_education.loc[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0] * 100, 1
    )


    # 6. Encontra o número mínimo de horas trabalhadas por semana
    # A função min() retorna o menor valor encontrado na coluna
    min_work_hours = df['hours-per-week'].min()


    # 7. Calcula a porcentagem de pessoas que trabalham o mínimo de horas e ainda assim ganham mais de 50K
    # Filtra as pessoas que trabalham exatamente o mínimo e calcula a proporção das que ganham mais de 50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        num_min_workers.loc[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0] * 100, 1
    )


    # 8. Encontra o país com a maior porcentagem de pessoas que ganham mais de 50K
    # Conta quantas pessoas em cada país ganham >50K
    country_salary_counts = df.loc[df['salary'] == '>50K', 'native-country'].value_counts()


    # Conta o total de pessoas por país
    country_total_counts = df['native-country'].value_counts()


    # Calcula a porcentagem de ricos por país e ordena em ordem decrescente
    # fillna(0) substitui valores ausentes por 0 para evitar erros de divisão
    country_percentages = (country_salary_counts / country_total_counts * 100).fillna(0).sort_values(ascending=False)


    # Identifica o país e o valor percentual mais alto
    highest_earning_country = country_percentages.index[0]
    highest_earning_country_percentage = round(country_percentages.iloc[0], 1)


    # 9. Encontra a ocupação mais comum entre pessoas que ganham >50K na Índia
    # Filtra registros onde o país é "India" e o salário é ">50K"
    # Usa mode() para obter a ocupação mais frequente (moda)
    top_occ_india = df.loc[
        (df['native-country'] == 'India') & (df['salary'] == '>50K'),
        'occupation'
    ].mode()[0]


    # Retorna todos os resultados em um dicionário para facilitar o acesso posterior
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_occ_india': top_occ_india
    }


# Bloco principal — executa apenas se o arquivo for rodado diretamente
if __name__ == '__main__':
    # Cria um conjunto de dados fictício para teste local
    data = {
        'age': [39, 50, 38, 53, 28, 30, 45, 22, 33, 40],
        'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private',
                      'Private', 'Private', 'Private', 'Private', 'Private', 'Private'],
        'fnlwgt': [77516, 83311, 215646, 234721, 338409, 100000, 150000, 200000, 250000, 300000],
        'education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors', 'Masters', 'Doctorate', 'HS-grad', 'Bachelors', 'Masters'],
        'education-num': [13, 13, 9, 7, 13, 14, 16, 9, 13, 14],
        'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-civ-spouse',
                           'Married-civ-spouse', 'Never-married', 'Married-civ-spouse', 'Never-married',
                           'Married-civ-spouse', 'Married-civ-spouse'],
        'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Handlers-cleaners',
                       'Prof-specialty', 'Exec-managerial', 'Prof-specialty', 'Other-service', 'Adm-clerical', 'Exec-managerial'],
        'relationship': ['Not-in-family', 'Husband', 'Not-in-family', 'Husband', 'Wife', 'Not-in-family', 'Husband', 'Not-in-family', 'Wife', 'Husband'],
        'race': ['White', 'White', 'White', 'Black', 'Black', 'White', 'Asian-Pac-Islander', 'White', 'White', 'Asian-Pac-Islander'],
        'sex': ['Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female'],
        'capital-gain': [2174, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'capital-loss': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'hours-per-week': [40, 13, 40, 40, 40, 40, 40, 20, 40, 40],
        'native-country': ['United-States', 'United-States', 'United-States', 'United-States',
                           'Cuba', 'United-States', 'United-States', 'United-States', 'India', 'India'],
        'salary': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K', '>50K', '>50K', '<=50K', '>50K', '>50K']
    }


    # Converte o dicionário em um DataFrame
    dummy_df = pd.DataFrame(data)


    # Salva o DataFrame fictício em um arquivo CSV chamado 'adult.csv'
    dummy_df.to_csv('adult.csv', index=False)


    # Chama a função principal passando o arquivo recém-criado
    result = calculate_demographic_data('adult.csv')


    # Exibe os resultados no console, um por um
    for key, value in result.items():
        print(f"{key}:\n{value}\n")
