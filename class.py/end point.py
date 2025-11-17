def ts1():
    #create a user friendly welcome statement
    name = input(("please enter your name"))
    print(f'welcome {name}')
    goal = 10000
    steps = 7345
    per_of_goal = (steps / goal) * 100
    print(f'name your percent of goal is {per_of_goal}')
    remain = goal - steps
    print(f'name your remaining step is {remain}')



def ts2():
    #create an input statement to get the variables or data you need to calculate if they are over normal or under weight
    Weight = float(input("Weight(kg):  "))
    height = float(input("Height(m): "))
    BMI = Weight/(height**2)
    if BMI <= 18.5 or BMI < 25:
        print("Underweight")
    elif BMI  <=25 or BMI <30:
        print("Healthy")
    elif BMI >= 30:
        print("Overweight")



def ts3(Flag_user):
    Flag_user = False
    daily_screen_minutes = int(input("WHats your daily screen minutes "))
    steps = int(input("Whats your steps "))
    night_screen_minutes = int(input("Whats your night screen minutes: "))
    if daily_screen_minutes > 240 and steps < 5000:
        Flag_user = True
    elif night_screen_minutes > 60:
        Flag_user = True
    else:
        Flag_user = False    





def ts5():
    age = int(input("Enter Age: "))
    low_income = input("Are you registered as low income? (Yes/No): ").lower()
    free_class = input("Have you received a free class in the last 30 days? (Yes/No): ").lower()

    if age >= 16 and age <= 25:
        print("Eligible for free classes")
    elif low_income == "yes" and free_class == "no":
        print("Eligible for free class")
    else:
        print("Not eligible for free class")



def ts6():
    steps = int(input("Steps: "))
    water = int(input("Water (ml): "))
    point1 = (steps // 1000) * (water // 500)
    
    if point1 == 0 or point1 <= 19:
        print("Bronze")
    elif point1 >= 20 and point1 <=39:
        print("Silver: ")
    else:
        print("Gold")


def ts7():
    total_mins = int(input("Total minutes:  "))
    sessions = int(input("Sessions: "))
    Average_mins_per_session = total_mins /sessions
    #incomplete 



def summary_line():
    while True:
        steps = int(input("Steps: "))
        if steps < 0:
            print("Please enter a non-negative number for steps.")
        else:
            break

    while True:
        water_ml = int(input("Water (ml): "))
        if water_ml < 0:
            print("Please enter a non-negative number for water.")
        else:
            break

    while True:
        screen_mins = int(input("Screen minutes: "))
        if screen_mins < 0:
            print("Please enter a non-negative number for screen minutes.")
        else:
            break

    percent_steps = (steps * 100) // 10000
    water_points = (steps // 1000) * (water_ml // 500)
    screen_label = "OK" if screen_mins <= 240 else "High"

    return f"Steps: {steps} ({percent_steps}%), Water: {water_ml}ml (+{water_points} pts), Screen: {screen_mins} mins — {screen_label}"


print(summary_line())




    


    
    


   

