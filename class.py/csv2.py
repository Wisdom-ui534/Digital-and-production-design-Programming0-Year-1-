import csv

def menu():
    while True:
        choose = input("""
1. View scores
2. Add score
3. Exit
4. sort by score decending 
5. Print a simple leaderboard                                              
Choose an option: """)

        if choose == "1":
            view_scores()

        elif choose == "2":
            name = input("Enter name: ")
            score = get_valid_score()
            add_score(name, score)
        elif choose == "4":
            sort()
            

        elif choose == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
        
        


def get_valid_score():
    while True:
        value = input("Enter score: ")
        if value.isdigit():
            return int(value)
        print("Score must be a number. Try again.")


def add_score(user_name, score):
    with open("scores.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([user_name, score])
    print("Score added")


def view_scores():
    print("\nScores:")
    try:
        with open("scores.csv", "r") as file:
            reader = csv.reader(file)
            found = False
            for row in reader:
                print("Name:", row[0], " Score:", row[1])
                found = True
            if not found:
                print("No scores found")
    except FileNotFoundError:
        print("No score file found")


def sort():
    view_scores() = sorted(view_scores())
    print(view_scores())





