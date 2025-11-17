def Ts1():
    medication = input("""
                [M]. Medication saftey rule
                [F]. Fitness Centre Acess
                [S]. Sleep Tracker Alert
                [E]. Exit Terminal  """).lower()
    if medication == "m":
        Age = int(input("Enter Age: "))
        weight = float(input("Weight(kg):"))
        if Age > 12 and weight > 40:
            print("safe to give medicine")
        elif Age < 12 and weight < 40:
            print("Not safe to give medicine")
            Ts1()
    
    elif medication == "f":
        Age2 = int(input("Enter Age: "))
        have_medical_clearance = input("Do you have medical clearance?(Yes or No ) ").lower()
        if Age2 > 18 and have_medical_clearance == "yes":
            print("Eligible for intensive Zone")
            print(" Not Eligible for Intensive Zone")
            Ts1()
    elif medication == "s":
        sleep = input("Is the user asleep (yes/no) ").lower
        heart = int(input("Heart rate:  "))
        if sleep =="no" and heart > 100:
            print("......ALert Alert Alert .....")
    elif medication == "e":
        print("exit")
Ts1()
        
        
        
    


    


    
        
    