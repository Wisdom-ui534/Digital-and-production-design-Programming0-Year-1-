def validate_parcel_code(code):
   
    if len(code) != 7 or not code.isdigit():
        return "Invalid format (must be exactly 7 digits)"

    first_six = code[:6]
    check_digit = int(code[6])

    
    total = 0
    for i in range(6):
        digit = int(first_six[i])
        total += digit * (i + 1)

    calculated_digit = total % 10


    if calculated_digit == check_digit:
        return "Code is VALID"
    else:
        return "Code is INVALID"



incorrect_attempts = 0

while True:
    user_input = input("Enter a 7-digit parcel code (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    result = validate_parcel_code(user_input)
    print(result)

    if "INVALID" in result.upper():
        incorrect_attempts += 1

print(f"Number of incorrect attempts: {incorrect_attempts}")