import pandas as pd

# Create a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [25, 30, 35, 28],
    "Salary": [50000, 60000, 70000, 65000]
}

df = pd.Series(data, index = ["A", "B", "C", "D"] )

# Display the DataFrame
#print("Original DataFrame:")
#print(df)




fires = {
    'STATE': ['CA', 'TX', 'CA', 'NV', 'CA'],
    'FIRE_YEAR': [2010, 2011, 2012, 2012, 2013],
    'FIRE_SIZE': [500, 50, 2000, 300, 1200]

}
df = pd.DataFrame(fires)
    

#print(df)
fr = df[['STATE', 'FIRE_SIZE']]
#print(fr)

fl = df.iloc[2]
#print(fl)
ff = df[df['STATE'] == 'CA']
#print(ff)
BF = df[df['FIRE_SIZE'] > 1000]
#print(BF)



#Activity
import pandas as pd

animals = {
    'ANIMAL': ['Dog', 'Cat', 'Dog', 'Bird', 'Cat'],
    'AGE': [5, 3, 2, 1, 7],
    'WEIGHT': [20, 5, 25, 1, 4]
}

#show the entire data frame
df = pd.DataFrame(animals)
print(df)
#show only the animal column
animal_coloum = df['ANIMAL']
print(animal_coloum)
#show the first two rows of the dataframe
first_two_coloum = df.iloc[:2]
print(first_two_coloum)
#show all roll where AGE is greater than 4 
greater = df[df['AGE'] > 4]
print(greater)
#add a new coloumn 

