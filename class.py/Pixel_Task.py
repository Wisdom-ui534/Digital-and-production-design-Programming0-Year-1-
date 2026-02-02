def Task_1():
    import pandas as pd
    #load the csv file into a pandas Dataframe
    df = pd.read_csv('pixelvault game sales.csv')
    print(df)
    #Display the first 5 rows of the dataset 
    print(df.head())
    #display the last 5 rowa of the dataset 
    print(df.tail())
    print(df.info())
Task_1()




def Task_2():
    import pandas as pd
    #display coloumn names 

    df = pd.read_csv('pixelvault game sales.csv')
    print("List of column names:", list(df.columns))
    #check data type
    data_type = df.columns
    print(type(data_type))

Task_2()




def Task_3():
    #check for missing value in the datasets 
    import pandas as pd
    df = pd.read_csv('pixelvault game sales.csv')
    print(df.isnull())
    #check for duplicate role 
    print(df.duplicated)
    #verify if total sale is calculated correctly (price * quantity)
    df['total_sale'] == df["price"] * df["quantity"]




Task_3()



