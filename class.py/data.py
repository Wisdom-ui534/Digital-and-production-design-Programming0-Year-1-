def Task_1():
    import pandas as pd
    df = pd.read_csv('lego_sets.csv')
    print(df)
    print(df.info())
    print(df.describe())


 
"""1.2 Dataset overview:  

- Number of rows: 12261 rows 
 
- Number of columns: 14 
- What does one row represent? Set_name 

 

 

 

 
 
1.3 Column understanding: 
Choose three columns and explain their purpose. 

Ages: This tells us the age range which the Lego toys fall under  

List_ prices: This tells us the estimated price of the Legos  

Num_reviews; This coloumn shows us the number of reviews the lego has  """

 




Task_1()

def Task_2():
 
    
 """2.1 Check data types 
Why is this important? 

It's important to check data types because they help to enforce code reliability and efficiency, making it easier to read and manipulate it. 

 

 
 
2.2 Missing data: 
Which columns contain missing values? 
How could missing data affect analysis? 

The presence of missing values can affect data analysis in multiple ways: first, it could reduce statistical power by and it may lead to estimation bias if missingness is not random; finally, it causes different variable analyses to rely on different subsets of samples. 

 

 

 

2.3 Summary statistics: 
What is the average LEGO price? 
What is the maximum LEGO price? 

The average Lego price is sum(list_price)/5 =£48.59 

The maximum Lego pirce = 99.990"""


def Task_3():
   import pandas as pd
   import matplotlib.pyplot as plt
   df = pd.read_csv('lego_sets.csv')
   plt.figure(figsize=(8,5))
   plt.hist(df["list_price"], bins=30, color="skyblue",edgecolor ="black ")
   plt.xlabel("LEGO price (£)")
   plt.ylabel("Number of sets")
   plt.title("Distribution of LEGO prices  ")
   plt.show()
   
#Task_3()

def Task_3b():
   import pandas as pd
   import matplotlib.pyplot as plt 
   df = pd.read_csv('lego_sets.csv')
   plt.figure(figsize=(8,5) )
   plt.scatter(df["piece_count"], df["list_price"], alpha=0.6)
   plt.xlabel("Number of pieces")
   plt.ylabel("price(£)")
   plt.title("LEGO pieces count vs price  ")
   plt.show()


Task_3b()

def Task_4():
   import pandas as pd
   import matplotlib.pyplot as plt 
   df = pd.read_csv('lego_sets.csv')
   plt.figure(figsize=(8,5))
   plt.hist(df["play_star_rating"],bins = 30, color="blue",edgecolor ="black " )
   plt.xlabel = ("Rating")
   plt.ylabel=("Rating")
   plt.title("Top 10 LEGO themes by rating")
   plt.show()



   
   