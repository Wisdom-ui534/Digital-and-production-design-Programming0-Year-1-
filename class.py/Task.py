def TS1():
    Test_type = str(input("What is the test type (glucose,cholesterol) ")).lower()

    if Test_type == "glucose":
        value = float(input("whats the current value (in mmol/g) "))
        value_mdgl = value * 18.010 / 10
        print(f'{value_mdgl} is your result in mg/dl')
    elif Test_type == "cholesterol":
        value2 = float(input("What is your current unit (in mmol/g ) "))
        value2_mdgl = value2 * 38.67
        print(f'{value2_mdgl} is your result in mg/dl')
    else:
        print("Please enter glucose or chlesterol" )
TS1()


  

def TS2():
    Temp1 = float(input("Enter the first temprature in celcius "))
    Temp2 = float(input("Enter the second temprature in celcius "))
    Temp3 = float(input("Enter the third temprature in celcius "))
    Average = (Temp1 + Temp2 + Temp3 / 3)
    if Average >= 38:
        print("Temprature exceeds the fever threshold constant ")
    elif Average < 38:
        print("Temprature does not exceeds the fever threshold constant ")
    else:
        print("................")
TS2()

def TS3():
    Age = int(input("Whats your age "))
    if Age >= 18:
        h = float(input("Whats your heart rate"))
        if h >= 60 and h <= 100:
            print("Your heart rate is normal")
        elif h > 100 or h < 60:
            print("your heart rate is not normal please seek medical advice immediately.....")
    elif Age < 18:
        hr = float("whats your heart rate   ")
        if hr >= 60 and hr <= 100:
            print("your heart rate is normal have a lovely day ")
        elif hr > 100 or hr < 60:
            print("your heart rate is not normal please seek medical advice..")
    else:
        exit()
TS3()


