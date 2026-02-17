import random

def Math_quiz():
    flag = True
    while flag:
        print("############### Welcome to the Random Quiz Generator ############")
        print("###############    1. Maths Quiz     ############")
        print("###############    2. Exit Terminal  ############")

        choice = input("Please enter your choice: ")

        if choice in ["1", "2"]:
            print("Choice accepted")
            flag = False
        else:
            print("Sorry, you did not enter a valid option")

    return choice


def Math_quiz_menu():
    flag = True

    while flag:
        print("\n#########################################################################")
        print("##################### Great you have clicked Maths quiz ################")
        print("#########################################################################")
        print("######## Please select an option ###########")
        print("######### 1. Generate Maths Question #######")
        print("######### 2. Exit to Main Menu #############")

        choice2 = input("Enter the number selection here: ")

        if choice2 in ["1", "2"]:
            print("Choice accepted!")
            flag = False
        else:
            print("Sorry you did not enter a valid option")

    return choice2


def generate_maths_question():
    print("########## Please answer the following maths question below ##########")

    num1 = random.randint(2, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-'])

    if operator == '+':
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2

    user_answer = int(input(f'What is {num1} {operator} {num2}? '))

    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f'Wrong, the answer was {correct_answer}.')


# Main program
main_menu_choice = Math_quiz()

if main_menu_choice == "1":
    total_menu_choice = Math_quiz_menu()

    if total_menu_choice == "1":
        generate_maths_question()

elif main_menu_choice == "2":
    print("Exiting program...")
