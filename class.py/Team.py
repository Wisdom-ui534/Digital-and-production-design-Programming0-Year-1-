
    

def start():
     import pandas as pd
     import math
     import random
     import numpy as np 

     df =pd.read_csv('GameShop.csv')


     mean = df['Total Revenue'].mean()
     print("Mean of the total revenue :")
     print(mean)

 
     revenue = df['Total Revenue']

   
     std_dev = np.std(revenue)
     max_rev = np.max(revenue)
     min_rev = np.min(revenue)

   
     mean_rev = revenue.mean()
     sqrt_mean = math.sqrt(mean_rev)

     print("Additional Calculations")
     print("Standard Deviation of Revenue:", std_dev)
     print("Maximum Revenue:", max_rev)
     print("Minimum Revenue:", min_rev)
     print("Square Root of Mean Revenue:", sqrt_mean)



start()




def read():
      import pandas as pd
      df =pd.read_csv('GameShop.csv')
      print(df)

read()


     





def vis1():
    import matplotlib.pyplot as plt
    import pandas as pd
    df = pd.read_csv("GameShop.csv")
    
    category_sales = df.groupby('Category')['Units Sold'].sum()
    
    plt.figure(figsize=(8,5))
    plt.bar(category_sales.index, category_sales.values)
    plt.xlabel("Category")
    plt.ylabel("Units Sold")
    plt.title("Units Sold per Category")
    plt.xticks(rotation=45)
    plt.show()

vis1()



def vis2():
     
     import matplotlib.pyplot as plt
     import pandas as pd
     df = pd.read_csv('GameShop.csv')
     category_sales2 = df.groupby('Category')['Price'].sum()
     plt.figure(figsize=(8,5))
     plt.bar(category_sales2.index, category_sales2.values)
     plt.xlabel("Category")
     plt.ylabel("Price")
     plt.title("Price per category ")
     plt.xticks(rotation=45)
     plt.show()


vis2()


def vi3():
     import matplotlib.pyplot as plt
     import pandas as pd

     df = pd.read_csv('GameShop.csv')

     category_sales2 = df.groupby('Category')['Price'].sum()

     plt.figure(figsize=(8,5))
     plt.pie(category_sales2.values, labels=category_sales2.index, autopct='%1.1f%%')
     plt.title("Price per category")
     plt.show()


vi3()
     







