import pandas as pd

#Outputs the main menu and checks the user input
def main_menu():
    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("1. Total sales by product")
        print("2. Total sales of product category ")
        print("3. Total income by product")

        choice = input('Enter your number selection here: ')

        if choice.isdigit():
            flag = False
        else:
            flag = True

    return int(choice)


#Generates submenu of available product codes and allows user to select a product to view
def get_product_category ():
    df = pd.read_csv("T4a.csv")
    product_category = df["Category"].unique().tolist()
    flag = True

    while flag:
        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("Select a product category:")
        for i in range(len(product_category)):
            print(i+1, " ", product_category[i])
            selection = input('Enter your number selection here: ')

        if selection.isdigit():
            selection = int(selection)
            flag = False
        else:
            flag = True

        product_cat = product_category[selection -1]
   
    print("You have selected product id:",product_cat)
    return product_cat
















def get_product_id ():

    df = pd.read_csv("T4a.csv")

    product_codes = df["Product ID"].unique().tolist()

    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("Select a product code:")
        for i in range(len(product_codes)):
            print(i+1, " ", product_codes[i])

        selection = input('Enter your number selection here: ')

        if selection.isdigit():
            selection = int(selection)
            flag = False
        else:
            flag = True

        
        product_ID = product_codes[selection -1]
   
    print("You have selected product id:",product_ID)
    return product_ID

#gets and converts user input from string to date format
def get_date(start_end):
    
    flag = True
    
    while flag:
        date = input('Please enter {} date for your date range (DD/MM/YYYY) : '.format(start_end))

        try:
           pd.to_datetime(date, format="%d/%m/%Y")
        except ValueError:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return date
def get_data_by_category_and_date(cat, start_date, end_date):
    all_data = pd.read_csv("T4a.csv")
    product_data = all_data.loc[all_data["Category"] == cat].copy()

    product_data["Date"]= pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")
    date_range = (product_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                  (product_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    extracted_data = product_data.loc[date_range]

    return extracted_data
    

def get_income_by_ID_and_date(product_id, start_date, end_date):
    all_data = pd.read_csv("T4a.csv")
    product_data = all_data.loc[all_data["Product ID"] == product_id].copy()

    product_data["Date"]= pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")
    
    date_range = (product_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                  (product_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    
    extracted_data = product_data.loc[date_range]

    return extracted_data
    






    

#extracts data based on product ID within a user specified date range.
def get_data_by_ID_and_date(product_id, start_date, end_date):
    all_data = pd.read_csv("T4a.csv")
    product_data = all_data.loc[all_data["Product ID"] == product_id].copy()

    product_data["Date"]= pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")
    
    date_range = (product_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                  (product_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    
    extracted_data = product_data.loc[date_range]



    return extracted_data
def calculate_total_sale_for_category (date_ID, product_id, start_date, end_date):
     total_sales = date_cat["Qty Sold"].sum()
     print('The total number of sales for product category  {}, between {} and {} was: {}'.format(cat, start_date, end_date, total_sales))
     

def calculate_total_income_for_product (date_ID, product_id, start_date, end_date):
    df = pd.read_csv("T4a.csv")

    total_income_cal = df["Qty Sold"] * df["Price"]
    total_income = date_ID[total_income_cal].sum()
    print('The total income of sales for product {}, between {} and {} was: {}'.format(product_id, start_date, end_date, total_income))








#generates a total of the number of items sold for the extracted data
def calculate_total_sale (date_ID, product_id, start_date, end_date):
    total_sales = date_ID["Qty Sold"].sum()
    print('The total number of sales for product {}, between {} and {} was: {}'.format(product_id, start_date, end_date, total_sales))


main_menu_choice = main_menu()

if main_menu_choice == 1:
    product_id = get_product_id()
    start_date = get_date("start")
    end_date = get_date("end")
    date_ID = get_data_by_ID_and_date(product_id, start_date, end_date)
    calculate_total_sale (date_ID, product_id, start_date, end_date)

elif main_menu_choice == 2:
    cat = get_product_category()
    start_date = get_date("start")
    end_date = get_date("end")
    date_cat = get_data_by_category_and_date(cat, start_date, end_date)
    calculate_total_sale_for_category(date_cat, cat, start_date, end_date)

elif main_menu_choice == 3:
    product_id = get_product_id()
    start_date = get_date("start")
    end_date = get_date("end")
    date_ID = get_income_by_ID_and_date(product_id, start_date, end_date)
    calculate_total_income_for_product(date_ID, product_id, start_date, end_date)


    


