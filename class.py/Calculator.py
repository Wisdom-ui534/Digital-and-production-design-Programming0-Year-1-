def cal():
    import math
    Ask = float(input("Enter a number ........."))
    square_r = math.sqrt(float(Ask))
    square = Ask ** 2
    print(f'Square root of {Ask} is {square_r}')
    print(f'The square of {Ask} is {square}')
    Round_up = math.ceil(square_r)
    print(f'The square root rounded up is: {Round_up}')
    Round_down = math.floor(square_r)
    print(f'The square root rounded up is: {Round_down}')
    Area_of_circle = 22/7 * square
    print(f'Using the nuber you entered as the radius, the area of the circle is {Area_of_circle}')



#cal()



def Dice():
    import random 
    First_dice = random.randint(1,6)
    Second_dice = random.randint(1,6)
    
    option = input("Click 'R' to roll first dice  ").upper()
    print("Roling........")
    print(First_dice)
    option2 = input("Click 'R' to roll second dice ").upper()
    print("Rolling.......")
    print(Second_dice)
    total = First_dice + Second_dice
    if total == 7 or total ==  11:
        print("You win!")
    else:
        print("Try Again ")



       
        
    
Dice()



from datetime import datetime


now = datetime.now()
print(f"Today is: {now.strftime('%d/%m/%Y')}")


birth_year = int(input("Enter birth year: "))
birth_month = int(input("Enter birth month (1-12): "))
birth_day = int(input("Enter birth day (1-31): "))


age = now.year - birth_year
print(f"You are {age} years old.")


next_bd = datetime(now.year, birth_month, birth_day)

if next_bd < now:
    next_bd = datetime(now.year + 1, birth_month, birth_day)

days_till_next_bd = (next_bd - now).days
print(f"There are {days_till_next_bd} days until your next birthday!")





def Numpy():
    import numpy as np 
    weekly_sales = [120, 135, 150, 98, 175, 200, 143]
    print("The mean of the weekly sales: ")
    print(np.mean(weekly_sales))
    print(np.sum(weekly_sales))
    print(np.max(weekly_sales))
    print(np.min(weekly_sales))

Numpy()


def Final_challange():
    import random
    import numpy as np 
    import math
    random_number = random.randint(1,100)
    arr = np.array([random_number])
    Round = round(random_number)
    now = datetime.now()
    print(f"Today is: {now.strftime('%d/%m/%Y')}")


Final_challange()







