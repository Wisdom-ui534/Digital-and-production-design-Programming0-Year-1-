name = str(input("What is your first name"))
#ask the user for his or her first name
name2 = str(input("what is your last name"))
#ask for thier last name also
statement = (f'hello', name , name2 )
length_of_first_name = len(name)
print(f'the length of your first name is :', length_of_first_name)
length_of_second_name = len(name2)
print(f'the length of your second name is :', length_of_second_name)
#created a variable statement where i can print out a statement to the user 
if len(name) and len(name2) > 20:
    print("character limits exceeded")

else:
    print(statement)