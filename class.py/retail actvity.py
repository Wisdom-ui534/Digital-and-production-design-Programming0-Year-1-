def Task_1():
    import pandas as pd
    import matplotlib.pyplot as plt 
    cv = pd.read_csv('retail_sales_data.csv')
    print(cv)
    print(cv.head())
    print(cv.info())
    
    



#Task_1()

def Task_2():
    import pandas as pd
    
    csv_file_path = 'retail_sales_data.csv'
    df = pd.read_csv(csv_file_path)

    # Calculate total sale
    df['total_sale'] = df['quantity'] * df['price']

    # Save back to CSV
    df.to_csv(csv_file_path, index=False)

    print(df)
    import pandas as pd

# Load CSV
    csv_file_path = 'retail_sales_data.csv'
    df = pd.read_csv(csv_file_path)

# Calculate total revenue
    total_revenue = df['total_sale'].sum()

    print("Total revenue for the shop :", total_revenue)

# (Optional) save the dataframe back if needed
    df.to_csv(csv_file_path, index=False)
    #Total revenue per product 


    
#Task_2()



def Task_3():
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np 
    #Barchart
    #Revenue by products
    csv_file_path = 'retail_sales_data.csv'
    df = pd.read_csv(csv_file_path)
    x = np.array(df['products'])
    y = np.array(df['total_sale'])
    plt.bar(x,y)
    plt.show()

Task_3()











