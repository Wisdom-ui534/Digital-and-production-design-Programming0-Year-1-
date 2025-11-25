def Task():
    loan = [
        {
            "loan_id": 1,
            "student_name": "Alex Green",
            "student_id": "S12345",
            "device_type": "Laptop",
            "device_id": "L-001",
            "date_out": "2025-11-24",
            "due_back": "2025-12-01",
            "returned": False
        },
        {
            "loan_id": 2,
            "student_name": "Mila Stones",
            "student_id": "S12346",
            "device_type": "Laptop",
            "device_id": "L-002",
            "date_out": "2025-11-24",
            "due_back": "2025-12-01",
            "returned": False
        }
    ]

    menu = input("""
[1] Add a new loan 
[2] View all loan records
[3] Edit an existing loan 
[4] Remove a loan
[5] Exit application
Enter choice: """)

    if menu == "1":
        loan_id = input("Enter loan ID: ")
        student_name = input("Enter student name: ")
        student_id = input("Enter student ID: ")
        device_type = input("Enter device type: ")
        device_id = input("Enter device ID: ")
        date_out = input("Enter date out (yyyy-mm-dd): ")
        due_back = input("Enter due back date (yyyy-mm-dd): ")
        
        returned_input = input("Is the item returned? (True/False): ")
        returned = True if returned_input.lower() == "true" else False

       
        loan.append({
            "loan_id": loan_id,
            "student_name": student_name,
            "student_id": student_id,
            "device_type": device_type,
            "device_id": device_id,
            "date_out": date_out,
            "due_back": due_back,
            "returned": returned
        })

        print("Updated loan list:")
        for l in loan:
            print(l)
    elif menu == "2":
        for l in loan:
            print(l)
    elif menu == "3":
            edit_id = input("Enter the loan ID you want to edit: ")

            found = False
            for l in loan:
                if str(l["loan_id"]) == str(edit_id):
                    found = True
                    print(f"\nCurrent loan record: {l}")
                    print(f"Current 'returned' value: {l['returned']}")
                    
                    choice = input("Toggle returned value? (y/n): ").lower()

                    if choice == "y":
                        l["returned"] = not l["returned"]
                        print("Returned value has been toggled.")
                    else:
                        print("No changes made.")

                    print("Updated record:")
                    print(l)
                    break
    elif menu == "4":
        remove_id = input("Enter the loan id to be removed")
        if remove_id in loan:
            loan.remove(remove_id)
            print(f'{remove_id} has been succesfully removed')
        else:
            print("loan id not found....")
    elif menu == "5":
        print("Exiting the terminal ")
        
Task()
    



                    
    

