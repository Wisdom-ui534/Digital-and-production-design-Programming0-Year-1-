def Task():

  #creating a prgram for StrikeZone Company
  #First start the program by printing a welcome statement
  print("Welcome to StrikeZone Bowling & Café — where great games meet great flavors.")

  #Ask for the user's required personal  information  to improve the digital experience
  name = input("Please Enter your preffred name: ")
  print(f'{name}, please pick an option from the options below.....')

  #present a menu statement to the user
  while True:
    menu = input("""
                 [1]. Book a bowling lane
                 [2]. calculate prices
                 [3]. Process cafe order 
                 [4]. Store items
                 [5]. Display customer summary
                 [6]. Exit  
                 """)

    if menu == "1":
      phone_number = input("Please enter your phone number...")

      #  Phone number length check
      if len(phone_number) < 11:
        print("Invalid number")
      else:
        print("Phone number added")
        number_of_players = int(input("Enter number of players..."))
        if number_of_players > 6:
          print("Player limit exceeded, players must not exceed 6 people")
        else:
          print(f'{number_of_players} added successfully.....')

    elif menu == "2":
      print("Welcome to the pricing system , its £6 per hour")
      duration = float(input("How many hours do you want to book for..."))
      number = int(input("Please enter the number of lanes you need: "))

    
      price = number * 8 * duration
      print(f"Total price: £{price}")

      payment = input("How would you love to pay:"
                      "[1]. Debit card "
                      "[2]. Paypal "
                      "[3]. Vouchers ")

      if payment == "1":
        card_details = input("Please enter your card details: ")

   
        if len(card_details) != 16:
          print("Card number must be exactly 16 digits")
        else:
          n = input("Enter name on card: ")
          d = input("Enter expiring date: ")
          c = input("Enter cvc: ")
          conf = input("Are all details correct, and would you love to proceed to payment? yes/no ").lower()
          if conf == "yes":
            print("payment successful ")
          else:
            print("Payment cancelled")

      elif payment == "2":
        email = input("What's your email address: ")
        if "@gmail.com" in email:
          print("Validating payment.............")
          print("payment successful")
        else:
          print("Wrong email address, payment unsuccessful")

      elif payment == "3":
        print("Sorry, vouchers are unable to be processed for the meantime, please choose another method of payment")

    elif menu == "3":
      print("""
            coffee
            Shoe lace
            Bowling socks
            Wrist support
            Rosin bags
            Bowling tape
            Ball cleaner
            Mini towels
            Finger inserts  
            """)

    elif menu == "5":
      print("Here is the summary of all you bought:")

    elif menu == "6":
      print("Exiting the terminal")
      break

Task()
