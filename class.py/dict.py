schedule  = {"Wonka":"17:30", "Dune" :"19:15", "Inside out 2" : "20:00"}

machines = {
    "machine" : {
        "pinball Wizard " : "Pinball",
        "Dance Floor x" : "Rhythm",
        "Retro Racer" : "Racing",
        "Alien Blaster" : "Shooter"
        
    },
    "status" : {
        "pinball Wizard" : "Working",
        "Dance Floor x" : "Working",
        "Retro Racer" : "Needs service",
        "Alien Blaster" : "Working"

    }
}

def Ts2():
    cinema ={
        "Wonka" : {"Time" : "17:45", "Seats" : 45},
        "Dune 2" : {"Time" : "19:00", "Seats" : 30},
    }
    while True:
        menu = input("""
                     [1]. View all movies
                     [2]. Add a new movie
                     [3]. Book Tickets
                     [4]. Delete a movie
                     [5]. Validate seats counts 
                     [6]. Exit  """)
        if menu == "1":
            print(cinema)
        elif menu == "2":
            new = str(input("Enter new movie  "))
            newt = str(input("Enter the new movie time "))
            news = (int(input("Enter new movie's seat count ")))
            cinema[new] = (f'Time:{newt} seat count: {news} ')
            print(f'{new} has been sucessfully added ')
            print(cinema)
        elif menu == "3":
            book = input("Enter the movie you want to book for ")
            if book in cinema:
                print("You have sucessfully booked for " + book)
            else:
                print("Movie dosen't exist")
        elif menu == "4":
            delete = input("enter the movie you want to cancel ")
            if delete in cinema:
                cinema.pop(delete)
                print(f'{delete} sucessfully deleted ')
                print(cinema)
            else:
                print("Movie dosen't exist")
        elif menu ==  "5":
            seats = 45
            if book > seats:
                print("Oops No more space.............")
            else:
                print("Seats avlabile ")
            
        elif menu == "6":
            print("exit")
            break 
        else:
            print("Invalid cholice")


#Ts2()



def Ts3():
    print("How much do you know about the series 'Strangers things', lets find out together")
    quiz = {
        "Whats the first name of the character that got missing in season 1 of the series?" : "Will",
        "What US state is the show set in ?" : "Indiana",
        "In what year does the first season takes place" : 1982,
        "What food does Eleven loves to eat" : "Eggo waffles",
        "According to Hopper, mornings are for which two things?" : "Coffee and contemplation"

    }
    welcome = print("Try your best to answer these questions")
    for words in quiz:
        word = print(str(input(quiz.keys()))).lower()
        if word == quiz.values().lower():
            print("Congrats you got all corectly ")
        else:
            print("Not correct please try again ")
        


Ts3()
        



        

