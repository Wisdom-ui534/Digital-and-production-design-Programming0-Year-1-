
def Ts1():
    #Area of a rectangle = length * breadth
#first step is to ask the user for the length
    length = float(input("Length: "))
#now ask for breadth
    Breadth = float(input("Breadth: "))
#create a new variable that solves the area of  rectangle
    Area = length * Breadth
    #now print the area
    print(Area)
Ts1()



def T2():
    #in order to converty minutes into hours we have to divde the time unit in minutes by 60
    Time = float(input("How many minutes"))
    hours = Time / 60
    print(f'in hours : {hours}')
T2()

def T4():
    #When building a hospital project, we need useful data like the Patient's name, age and bill amount, in order to get this, we create an input statement so we can get responce back fro the patients
    Name = (input("Name: "))
    Age = int((input("Age: ")))
    bill = float(input("Whats your total bill (£) "))
    #create an if statement so if the user is under 18 we can apply discount
    if Age < 18:
        discount = bill -  (bill * 0.10) 
        print(f'Bill: {discount}')
    elif Age >= 18:
        print(f'Bill: {bill}')
    if bill > 1000:
        print("Bill must be 1000 or lower (£)") 
T4()

def T5():
    while True:
        password = input("Enter Password: ")
        
        confirm = input("Re enter password ")
        if confirm == password:
            print("Password sucessfully created")
            break 
        elif confirm != password:
            print("Password do not match")
T5()
 
def hospital():
    NAME=input("enter Patient Name: ")
    Age =int(input("AGE: "))
    height= float(input("height "))
    weight= float(input("WEIGHT" ))
    bmi= weight/height*height
    if bmi >= 25.0 and bmi < 30:
        print("overweight")
    elif bmi < 18.5:
        print("underweight")
    elif bmi >= 18.5 or bmi < 25:
        print("Normal weight")
    elif bmi >=  30:
        print("Obese")
    else:
        print("okay")
        
hospital()




   
