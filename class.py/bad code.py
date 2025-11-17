total_patients = 0

def add_patient():
    global total_patients
    total_patients += 1
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    print("Patient added:", name)

def view_total():
    print("Total patients:", total_patients)
add_patient()
view_total()