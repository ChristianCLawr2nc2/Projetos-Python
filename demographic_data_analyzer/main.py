import pandas as pd

def calculate_demographic_data(filepath):
    # Read the dataset
    df = pd.read_csv(filepath)

    # 1. How many people of each race are represented in this dataset?
    # This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df.loc[df['education'] == 'Bachelors'].shape[0] / df.shape[0] * 100, 1)

    # 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = round(advanced_education.loc[advanced_education['salary'] == '>50K'].shape[0] / advanced_education.shape[0] * 100, 1)

    # 5. What percentage of people without advanced education make more than 50K?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = round(lower_education.loc[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0] * 100, 1)

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(num_min_workers.loc[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0] * 100, 1)

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_salary_counts = df.loc[df['salary'] == '>50K', 'native-country'].value_counts()
    country_total_counts = df['native-country'].value_counts()
    country_percentages = (country_salary_counts / country_total_counts * 100).fillna(0).sort_values(ascending=False)
    highest_earning_country = country_percentages.index[0]
    highest_earning_country_percentage = round(country_percentages.iloc[0], 1)

    # 9. Identify the most popular occupation for those who earn >50K in India.
    top_occ_india = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K'), 'occupation'].mode()[0]

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


if __name__ == '__main__':
    # Example usage with a dummy dataset for local testing
    data = {
        'age': [39, 50, 38, 53, 28, 30, 45, 22, 33, 40],
        'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private', 


        'Private', 'Private', 'Private', 'Private', 'Private', 'Private'],
        'fnlwgt': [77516, 83311, 215646, 234721, 338409, 100000, 150000, 200000, 250000, 300000],
        'education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors', 'Masters', 'Doctorate', 'HS-grad', 'Bachelors', 'Masters'],
        'education-num': [13, 13, 9, 7, 13, 14, 16, 9, 13, 14],
        'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-civ-spouse', 'Married-civ-spouse', 'Never-married', 'Married-civ-spouse', 'Never-married', 'Married-civ-spouse', 'Married-civ-spouse'],
        'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Handlers-cleaners', 'Prof-specialty', 'Exec-managerial', 'Prof-specialty', 'Other-service', 'Adm-clerical', 'Exec-managerial'],
        'relationship': ['Not-in-family', 'Husband', 'Not-in-family', 'Husband', 'Wife', 'Not-in-family', 'Husband', 'Not-in-family', 'Wife', 'Husband'],
        'race': ['White', 'White', 'White', 'Black', 'Black', 'White', 'Asian-Pac-Islander', 'White', 'White', 'Asian-Pac-Islander'],
        'sex': ['Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female'],
        'capital-gain': [2174, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'capital-loss': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'hours-per-week': [40, 13, 40, 40, 40, 40, 40, 20, 40, 40],
        'native-country': ['United-States', 'United-States', 'United-States', 'United-States', 'Cuba', 'United-States', 'United-States', 'United-States', 'India', 'India'],
        'salary': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K', '>50K', '>50K', '<=50K', '>50K', '>50K']
    }
    dummy_df = pd.DataFrame(data)

    # Save the dummy data to a CSV file
    dummy_df.to_csv('adult.csv', index=False)

    # Call the function with the dummy data file
    result = calculate_demographic_data('adult.csv')

    # Print the results
    for key, value in result.items():
        print(f"{key}:\n{value}\n")