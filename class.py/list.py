def Ts1():
    songs = ['cool down by strei', 'Again by Wande coal', '21 by polo G', 'fun by rema', 'our time by lil tecca']
    songs.append('phonk')
    songs.remove('our time by lil tecca')
    songs.sort()
    print(len(songs))
    print(songs)


def Ts2():
    print("Welcome to the cinema booking System website  please choose an option ")
    movies = ['It,(Welcome to derry)', 'Madea Boo a Hollowen ', 'Haul out the holloween ', 'Spirit Halloween ', ]

    option = input("""
       [1]. View all movies
       [2]. Add a new movie
       [3]. Remove a movie
       [4].Find a movie
       [5].Exit  """)
    if option == "1":
        print(movies)
        Ts2()
    elif option == "2":
        new_movie = input("Enter new movie: ")
        movies.append(new_movie)
        Ts2()
    elif option == "3":
        Remove_movie = input("Enter the moovie you want to remove(double check to make sure there are no spelling errors)")
        movies.remove(Remove_movie)
        Ts2()
    elif option == "4":
        find_movie = input("Enter movie name ")
        if find_movie in movies:
            print(find_movie)
        else:
            print("sorry movie does not exist")
        Ts2()
    elif option =="5":
        print("Exit")
    else:
        print("Please choose a valid option")
#Ts2()


def Ts1():
    songs = ['cool down by strei', 'Again by Wande coal', '21 by polo G', 'fun by rema', 'our time by lil tecca']
    songs.append('phonk')
    songs.remove('our time by lil tecca')
    songs.sort()
    print(len(songs))
    print(songs)


def Ts2():
    print("Welcome to the cinema booking System website  please choose an option ")
    movies = ['It,(Welcome to derry)', 'Madea Boo a Hollowen ', 'Haul out the holloween ', 'Spirit Halloween ', ]

    option = input("""
       [1]. View all movies
       [2]. Add a new movie
       [3]. Remove a movie
       [4]. Find a movie
       [5]. Exit  """)
    if option == "1":
        print(movies)
        Ts2()
    elif option == "2":
        new_movie = input("Enter new movie: ")
        movies.append(new_movie)
        Ts2()
    elif option == "3":
        Remove_movie = input("Enter the movie you want to remove (double check to make sure there are no spelling errors): ")
        movies.remove(Remove_movie)
        Ts2()
    elif option == "4":
        find_movie = input("Enter movie name: ")
        if find_movie in movies:
            print(find_movie)
        else:
            print("Sorry, movie does not exist.")
        Ts2()
    elif option == "5":
        print("Exit")
    else:
        print("Please choose a valid option.")

# Ts2()


def Ts3():
    games = [
        '[1]. Call of Duty Mobile', '[2]. Fortnite', '[3]. Delta Force', 
        '[4]. Dream League', '[5]. Roblox', '[6]. Subway Surfers', 
        '[7]. Fruit Ninja', '[8]. Brawl Stars', '[9]. Sniper 3D'
    ]
    favourites = []  

    while True:
        print("""
        [1]. View games
        [2]. Add games to favourite
        [3]. Play game
        [4]. Exit
        [5]. View favourites      
        """)

        option = input("Choose an option: ")  

        if option == "1":
            print("Available games:")
            for game in games:
                print(game)  
        elif option == "2":
            print("Which game would you like to favourite?")
            for game in games:
                print(game)  
            favourite = input("Enter the game name to favourite: ")
            
            if any(favourite.lower() in game.lower() for game in games):
                favourites.append(favourite)
                print(f'{favourite} successfully added to your favourites!')
            else:
                print("Game not found in the list.")
        elif option == "3":
            game_to_play = input("Which game would you like to play? ")
            if any(game_to_play.lower() in game.lower() for game in games):
                print(f"Now playing {game_to_play}...")
            else:
                print("Game not found in the list.")
        elif option == "5":
            print("Your favourite games:")
            print(favourites)  
        elif option == "4":
            print("Exiting... Thank you for using the game list")
            break  
        else:
            print("Invalid option, please try again.")


#Ts3()


def Ts4():
    machines  = ["Pinball Wizard", "Dance Floor X", "Retro Racer", "Alien Blaster"] 
    categories = ["Pinball", "Rhythm", "Racing", "Shooter"] 
    status     = ["Working", "Working", "Needs Service", "Working"] 
    while True:
        print("""
              [1]. View all machines
              [2]. Add a machine
              [3].Update status(Working / Needs Service / Out of Order) 
              [4]. Filter by category
              [5]. list machine needing service
              [6]. Exit )""")
        option = input("choose an option ")
        if option == "1":
            for machine  in machines:
                print(machine)
        elif option == "2":
            print("What machine would you like to add")
            New = input("Enter machine: ").lower()
            new = input("Enter categories:  ").lower()
            neW = input("Enter status: ")  .lower() 
            New.append(machines).str
            new.append(categories).str
            neW.append(status).str
        #elif option == "3":
Ts4()