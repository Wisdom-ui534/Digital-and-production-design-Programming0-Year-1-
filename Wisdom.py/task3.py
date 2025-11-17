def BMI():
    name = input("Please what is your name ")
    weight = float(input("Whats your weight(in pounds) "))
    height = float(input("whats your height (in inches) "))
    imperial_measurment = weight / height**2 * 703
    if imperial_measurment < 18.5:
        print(f'{name} you are underweight')
    elif imperial_measurment >= 18.5  < 25 :
        print(f'{name} you have an Healthy weight')
    elif imperial_measurment >= 25 < 29.9:
        print(f'{name} you are overweight')
    elif imperial_measurment >= 30:
        print(f'{name} you are obese')
    else:
        print("Please enter your weight")
BMI()
    
    