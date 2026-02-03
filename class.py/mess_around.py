import pandas as pd
import matplotlib.pyplot as plt
try: 

    import pandas as pd
    Countries  = pd.read_csv('CountriesSD.csv')
    print(Countries)
    summer = pd.read_csv('SummerSD.csv')
    print(summer)
    Winter  = pd.read_csv('WinterSD.csv')
    print(Winter)
except FileNotFoundError:
    print("Dataset not found ")



# Schema Alignment
Winter.rename(columns={'Country': 'Code'}, inplace=True)
summer['Season'] = 'Summer'
Winter['Season'] = 'Winter'

# Concatenate
olympics = pd.concat([summer, Winter], ignore_index=True)

# Merge with Countries data
olympics_merged = olympics.merge(Countries, on='Code', how='left')

# Fill missing Country names
olympics_merged['Country'] = olympics_merged['Country_y'].fillna(olympics_merged['Country_x'])
olympics_merged.drop(columns=['Country_x', 'Country_y'], inplace=True)

print(f'Combined Data Shape: {olympics_merged.shape}')




season_counts = olympics_merged['Season'].value_counts()

plt.figure()
plt.pie(
    season_counts,
    labels=season_counts.index,
    autopct='%1.1f%%',
    startangle=90
)
plt.title('Distribution of Medals by Season')
plt.show()



gender_year = olympics_merged.groupby(['Year', 'Gender']).size().unstack()

gender_year.plot(kind='line')
plt.title('Gender Participation Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Athletes')
plt.show()



medals_year = olympics_merged.groupby('Year')['Medal'].count()

plt.plot(medals_year.index, medals_year.values)
plt.title('Growth of Olympic Medals Over Time')
plt.xlabel('Year')
plt.ylabel('Total Medals')
plt.show()
