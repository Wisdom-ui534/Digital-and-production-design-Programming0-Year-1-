def vsm():
    while True:
        welcome = input("""Welcome to the Vital Signs Monitor , please choose from the following options
                    t - To check the state of your temprature 
                    o - to check your oxygen level 
                    h - to check heart rate  
                    e -  to exit """).lower()
        if welcome == "t":
            temp = float(input("Please enter temprature on celicus "))
            if temp > 37.5:
                print("High temprature")
            elif temp  < 37.5:
                print("low temprature")
                
            
        elif welcome == "o":
            oxy = int(input("please enter oxygen rate "))
            if oxy < 92:
                print("low oxygen please visit your GP")
            else:
                print("normal oxygen rate")

        elif  welcome == "h":
            heart = int(input("Please enter heart rate "))
            if heart <= 60 or heart <= 100:
                print("Normal heart rate")
            else:
                print("Heart rate not normal please visit your doctor ")
        elif welcome == "e":
            break 
#vsm()

def app():
    #ask for the health data
    glucose  = float(input(" please enter your glucose level as of last week,"))
    print("great, thanks for the useful information")
    glucose2 = float(input("Please enter your glucose level for this weeek "))
    if glucose > glucose2:
        print("congratulations, they has been great improvement, please keep up the good work")
    elif glucose < glucose2:
        print("Sorry to break it to you but there hasn't been any improvement made, please try to see your doctor this week.")
    elif glucose == glucose2:
        print("Still the same, nothing changed, if comfortable, please seek for medical advice")
app()
    
#The diffrence between the operator = and == is that th efirst one which is the equal sign is uused for equality example 2 + 2 = 4. whil the other one is more of similarity.
#its like saying that two thinkgs look alike or are the same example 2==2, 400 == 400.

#example of whgen we use  >=:
#we use this if we want the particular numeric value and the numbers higher or lower than it to be affected.
# How do arithimetic and relational operators work together? : Arithmetic and relational operators work together in expressions by following a specific order of precedence

    

    


    


