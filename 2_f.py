phone_num = input("Please enter your phone number (numbers only)\n")
while True:
    if not phone_num.isnumeric():
        phone_num = input("The phone number is not contain only numbers, please try again\n")
    elif len(phone_num) < 10:
        phone_num = input("The phone number is too short and contain 10 digit number, please try again\n")
    elif len(phone_num) > 10:
        phone_num = input("The phone number is too long and contain 10 digit number, please try again\n")
    else:
        break

print(f"The phone number is: {phone_num}")