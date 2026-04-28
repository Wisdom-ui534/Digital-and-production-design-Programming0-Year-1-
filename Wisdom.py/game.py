def simple_text_based_adventure():
    print("----------------")
    print("Shadowed Souls")
    print("---------------")
    while True:
        name = input("Whose soul has been encountered today? ")
        print(f"Welcome {name} to the House of the Shadowed Souls")
        cont = input("""History tells us that this house has been haunted since the 1870s, when people hid here to escape the war.

It is said that their souls still linger, and ghosts continue to roam these halls.

Do you still wish to enter?

If you have second thoughts and wish to go back, press 'B', else press 'E' to enter the house.
""").upper()

        if cont == "B":
            print("As your heart leads,", name, "quietly leaves the haunted house")
            print("Exiting game.......")
            break

        elif cont == "E":
            print(name, "enters the house....")
            print("The lights in the house are dimmed...")
            print("The doors behind you turn to smooth flat walls.....")
            print("You are greatly in shock and fear has engulfed you")
            print("The light turns off.....")
            print("You quickly turn on your flashlight you held with you as you went in")
            print("You move forward a little, you come across 2 doors (a red and a green door)")
            
            door_choice = input("Enter 'G' to enter the green door or press 'R' to enter the red door or 'B' to go back: ").upper()

            if door_choice == 'G' or door_choice == 'R':
                print("You try to open the door... but then you notice it's locked. You try all spare keys you have, but it does not work.")
                print("Mission: Get the key and open the door.")
                print("You try the other door too but it does not open")
                print("You look around, then you find some stairs.....")
                print("At the top of the stairs you see a key lying on the floor")
                print("You take your first step, then you hear a noise.")
                print("You quickly look up.")
                print("Then you see a shadow-like person")
                print("Out of fear you ask, who is there")
                print("But there's no response, and the shadow-like human walks away and vanishes into the wall")
                print("With fear, you quickly run up, get the key, and go back to the doors")
                print("On getting to the door scene, you notice that the doors have become one, and this time it is a black door.")
                
                open_choice = input("Press 'O' to open the door: ").upper()
                if open_choice == "O":
                    print("You opened the door.......")
                    print("First Mission Passed!")

            elif door_choice == "B":
                print("You try to find an escape and then suddenly a hand grabs your neck from behind and eliminates you")
                print("Mission failed.....")

simple_text_based_adventure()