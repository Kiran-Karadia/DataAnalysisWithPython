import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    index = df['race'].unique()
    no_of_each_race = []
    for race in index:
        no_of_each_race.append(len(df.loc[df['race'] == race]))
    race_count = pd.Series(no_of_each_race, index)
    

    # What is the average age of men?
    average_age_men = round(sum(df['age'][df['sex']=="Male"]) / len(df['age'][df['sex']=="Male"]), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df.loc[df['education'] == "Bachelors"])/len(df))*100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # percentage with salary >50K
    all_advanced = len(df.loc[(df['education']=="Bachelors") | (df['education'] == "Masters") | (df['education'] == "Doctorate")])
    higher_education = len(df.loc[(df['education']=="Bachelors") | (df['education'] == "Masters") | (df['education'] == "Doctorate")])
    
    
    all_not_advanced = len(df.loc[((df['education'] != "Bachelors") & (df['education'] != "Masters") & (df['education'] != "Doctorate"))])
    lower_education = len(df.loc[((df['education'] != "Bachelors") & (df['education'] != "Masters") & (df['education'] != "Doctorate"))])

    # percentage with salary >50K
    advanced_above_50K = len(df.loc[((df['education']=="Bachelors") | (df['education'] == "Masters") | (df['education'] == "Doctorate")) & (df['salary'] == ">50K")])
    not_advanced_below_50k = len(df.loc[((df['education'] != "Bachelors") & (df['education'] != "Masters") & (df['education'] != "Doctorate") & (df['salary'] == ">50K"))])
    
    higher_education_rich = round((advanced_above_50K / all_advanced) * 100, 1)
    lower_education_rich = round((not_advanced_below_50k / all_not_advanced * 100), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df.loc[df['hours-per-week'] == 1])
    num_min_works_above_50K = len(df.loc[((df['hours-per-week'] == 1) & (df['salary'] == ">50K"))])
    rich_percentage = round((num_min_works_above_50K / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    rich_in_country = df.loc[df['salary'] == ">50K"]['native-country'].value_counts()
    total_in_country = df['native-country'].value_counts()
    percentages = pd.Series(round((rich_in_country/total_in_country)*100, 1))
    
    highest_earning_country = percentages[percentages==percentages.max()].index[0]
    highest_earning_country_percentage = percentages[percentages==percentages.max()][0]

    # Identify the most popular occupation for those who earn >50K in India.
    india_above_50K = df.loc[df['native-country']=="India"]
    top_IN_occupation = india_above_50K['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
