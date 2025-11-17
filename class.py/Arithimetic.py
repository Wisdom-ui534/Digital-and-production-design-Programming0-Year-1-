def fitness():
    #create a friendly and welcoming interface for the user
    Welcome = str(input("""
                        Welcome to my fitness app please  inspect and choose one out of the following option 😄
                        .c - to check Calorie burn ⊹₊🔥⋆｡°✩
                        .s - for step conversion 👣
                        .m- for medication timing ⏱️
                        .p - to check Medicine pack usage 💊
                        .h - to check Heart recovery ❤️‍🩹
                        .or any other letter  - to exit """)).lower()

    #Then for each step create an onterface
    if Welcome == "c":
        #ask for the calorie/minute ask required from the task
        calories = int(input("please input Calorie per minute "))
        #Ask for the workout time / in minutes
        workout= float(input("Please input your work out time /in minutes "))
        #now using the data collected from the user we calculate the calorie burn
        calorie_burn = calories * workout
        #print out a statement telling the user their result
        print(f'here is your result {calorie_burn}')
        fitness()
        #create an interface for the second option
    elif Welcome == "s":
        #ask for the number of steps the user has walked
        steps = int(input("Enter total steps "))
        #using the given formula, convert the steps
        step_conv = steps / 1300
        #Printa s statement telling the user the distance in kilometer
        print(f'dinstance in km = {step_conv}')
        fitness()
    elif Welcome == "m":
        #ask the user to enter the total minutes
        min = int(input("Enter Total minutes "))
        #Now estimate and roundup the hours so that it appears as a whole number
        Medication_timing = min // 60
        # now derrive the minutes
        medication = min - (Medication_timing * 60)
        #Finally print both on the  terminal
        print(f'{Medication_timing} hours {medication} minutes')
        fitness()
    elif Welcome == "h":
        heart_rate = float(input("Please enter your heart rate when excersicing "))
        heart = float(input("Please enter your heart rate when you are at rest "))
        Recovery_rate = heart_rate - heart
        print(f' here is your result {Recovery_rate} ')
        fitness()
    elif Welcome == "e":
        print("exit")
fitness()


#def menu():
    #start = input("Welcome to my Health care Healper") 


        


    

