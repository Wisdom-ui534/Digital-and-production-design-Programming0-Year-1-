def Task1():
    #load the data set
    import pandas as pd
    df = pd.read_csv('amazon_sales_dataset.csv')
    print(df)
    #find number of rows  and coloumns 
    print(df.info())


    
Task1()

def Task2():
    #calculate total and average sales value
    import pandas as pd
    df = pd.read_csv('amazon_sales_dataset.csv')
    df['Total sales value'] = df['quantity_sold'] * df['price']
    print(f'Total sales value: {df["Total sales value"]}')
    #Average sales value
    df['Average sales value '] = df['total_revenue'] / df['Total sales value']
    print(f'Average sales value : {df["Average sales value "]}')






Task2()



def Task3():
    import pandas as pd
    import matplotlib.pyplot as plt

    
    df = pd.read_csv('amazon_sales_dataset.csv')

    # Group by category and sum sales
    sales_by_category = df.groupby('product_category')['total_revenue'].sum()

   
    plt.figure(figsize=(10, 6))
    sales_by_category.plot(kind='bar')

   
    plt.title("Total Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")

   
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    plt.show()

Task3()



def Task4():
    #analyse sales by region
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('amazon_sales_dataset.csv')
    #group by region and sales
    sales_by_region = df.groupby('customer_region') ['total_revenue'].sum()
    plt.figure(figsize=(10, 6))
    sales_by_region.plot(kind="bar")

    plt.title("Total sales by customer region ")
    plt.xlabel("Customer region")
    plt.ylabel("Total sales ")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()



Task4()


    
