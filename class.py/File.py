with open("scores.txt", "w") as file:
    file.write("Wisdom: 90\n")
  




with open("scores.txt", "r") as file:
    lines = file.readlines()       


for line in lines:
    print(line.strip())            


print("Number of lines:", len(lines))




def Task_3():
    name = input("Enter name ")
    score = input("Enter score")
    with open("scores.txt", "a") as file:
        file.write(f'{name} : {score}\n')
        print("Score saved")
    
    option = input("Do you want to view all scores? (y/n").lower()
    if option == "y":
        view_score()


def view_score():
    print("----Previous score:----   ")
    try:
        with open("scores.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("No score saved yet.")
                return 
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print("No score file found ")

Task_3()

