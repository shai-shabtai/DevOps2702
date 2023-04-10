def get_number():
    number = input("Please Enter a number:\n")
    while True:
        if not number.isnumeric():
            number = input("Your number is not valid, Please Enter a number:\n")
        else:
            return number


def sum_digit(number):
    sum_of_digits = 0
    for i in range(len(number)):
        sum_of_digits += int(number[i])
    return sum_of_digits


print(f"The sum of digits is: {sum_digit(get_number())}")
