import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Task_4a.csv')


def mainmenu():
    print("\t\t****Welcome to the Dashboard****")
    print('1) Return all current data')
    print('2) Return data for a specific region')
    print('3) Return data for diffrent size of property within a region' )
    return int(input(""))


def alldata():
    print(df)


def region_check(region, startdate, enddate):  # region, startdate, enddate

    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']

    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    ave = df1.mean()
    ave.plot()
    plt.show()
    return result

def region2_check(region2,startdate2, enddate2):
    df3 = df.loc[:, startdate2:enddate2]
    df4 =df.loc[:, 'Region code' : 'Rooms']

    result2 = pd.concat([df4, df3],axis=1, join='inner').where(df4["Region"] == region2)
    result2 = pd.DataFrame(result2)
    print(result2)
    ave2 = df3.mean()
    ave2.plot()
    plt.show()
    return result2

def property_check(property,startdate2, enddate2):
    df5 =df.loc[:, startdate2:enddate2]
    df6 =df.loc[:, 'Property Type' : 'Propertys']


    result3 = pd.concat([df6, df5],axis=1, join='inner').where(df6["Property Type"] == property)
    print(result3)
    ave3 = df5.mean()
    ave3.plot()
    plt.show()
    return result3
    
    

x = mainmenu()
while x == 1 or x == 2 or x == 3:
    if x == 1:
        alldata()

    elif x == 2:
        while True:
            print()

            region = input("Please enter the name of the region you would like to check:")
            region = region.capitalize()
            if region in df.Region.values:
                while True:
                    startdate = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. JAN-20")
                    startdate = startdate.capitalize()
                    if startdate not in df.columns:
                        print("Error start date not found")
                    else:
                        while True:
                            enddate = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. JAN-20")
                            enddate = enddate.capitalize()
                            if enddate not in df.columns:
                                print("Error end date not found")
                            else:
                                region_check(region, startdate, enddate)
                                break
                        break
                break
    elif x == 3:
            while True:
                print()
                region2 = input("Please enter the name of the region you would like to check:")
                region2 = region2.capitalize()
                if region2 in df.Region.values:
                    while True:
                        startdate2 = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. JAN-20")
                        startdate2 = startdate2.capitalize()
                        if startdate2 not in df.columns:
                            print("Error start date not found ")
                        else:
                            while True:
                                enddate2 = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. JAN-20")
                                enddate2 = enddate2.capitalize()
                                if enddate2 not in df.columns:
                                    print("Error end date  not found ")
                                
                                else:
                                    while True:
                                        property = input("PLEASE ENTER PROPERTY TYPE ")
                                        
                                        if property not in df.PropertyType.values:
                                           
                                            print("Error,Property type not found ")
                                         
                                        else:
                                            property_check(property,startdate2,enddate2)
                                            break
                                    break
                            break
                                    


            else:
                print("Region not found")

    x = mainmenu()



