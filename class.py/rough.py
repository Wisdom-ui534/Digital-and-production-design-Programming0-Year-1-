def Ts4():
    machines  = ["Pinball Wizard", "Dance Floor X", "Retro Racer", "Alien Blaster"] 
    categories = ["Pinball", "Rhythm", "Racing", "Shooter"] 
    status     = ["Working", "Working", "Needs Service", "Working"] 
    
    while True:
        print("""
              [1]. View all machines
              [2]. Add a machine
              [3]. Update status (Working / Needs Service / Out of Order) 
              [4]. Filter by category
              [5]. List machines needing service
              [6]. Exit""")
        option = input("Choose an option: ")
        
        if option == "1":
            print("\nMachine Name - Category - Status")
            for i in range(len(machines)):
                print(f"{machines[i]} - {categories[i]} - {status[i]}")
                
        elif option == "2":
            print("What machine would you like to add?")
            new_machine = input("Enter machine name: ")
            new_category = input("Enter category: ")
            new_status = input("Enter status (Working / Needs Service / Out of Order): ")
            
            # Add new machine, category, and status to the lists
            machines.append(new_machine)
            categories.append(new_category)
            status.append(new_status)
            print(f"{new_machine} has been added successfully!\n")
        
        elif option == "3":
            print("Which machine's status would you like to update?")
            for i, machine in enumerate(machines):
                print(f"{i + 1}. {machine}")
            
            try:
                machine_choice = int(input("Enter the number of the machine: ")) - 1
                if machine_choice < 0 or machine_choice >= len(machines):
                    print("Invalid choice. Try again.")
                    continue
                new_status = input("Enter new status (Working / Needs Service / Out of Order): ")
                status[machine_choice] = new_status
                print(f"The status of {machines[machine_choice]} has been updated to {new_status}.\n")
            except ValueError:
                print("Please enter a valid number.\n")

        elif option == "4":
            filter_category = input("Enter category to filter by (Pinball, Rhythm, Racing, Shooter): ").capitalize()
            print(f"\nMachines in the {filter_category} category:")
            found = False
            for i in range(len(categories)):
                if categories[i] == filter_category:
                    print(f"{machines[i]} - {status[i]}")
                    found = True
            if not found:
                print("No machines found in that category.\n")

        elif option == "5":
            print("\nMachines needing service:")
            found = False
            for i in range(len(status)):
                if status[i] == "Needs Service":
                    print(f"{machines[i]} - {categories[i]} - {status[i]}")
                    found = True
            if not found:
                print("No machines need service at the moment.\n")

        elif option == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please choose a valid option.\n")

Ts4()
