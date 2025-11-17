total_students = 0

def add_students(total_students):

    total_students += 1
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    print("Student added:", name)
    return total_students

def view_total(total_students):
    print("Total students:", total_students)
def reset_total(total_students):
    total_students = 0
    return total_students
total_students = add_students(total_students)
total_students = add_students(total_students)
total_students = add_students(total_students)

view_total(total_students)
total_students = reset_total(total_students)
view_total(total_students)




