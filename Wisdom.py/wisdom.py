def TS2():
    Temp1 = float(input("Enter the first temprature in celcius"))
    Temp2 = float(input("Enter the second temprature in celcius"))
    Temp3 = float(input("Enter the third temprature in celcius"))
    Average = (Temp1 + Temp2 + Temp3 / 3)
    if Average >= 38:
        print("Temprature exceeds the fever threshold constant")
    elif Average < 38:
        print("Temprature does not exceeds the fever threshold constant")
    else:
        print("................")
TS2()