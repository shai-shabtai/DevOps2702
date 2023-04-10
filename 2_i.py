def add_numbers(num1, num2):
    return num1 + num2


def add_space_to_strings(string1, string2):
    return string1 + " " + string2


num1 = 2
num2 = 5
str1 = "Hello"
str2 = "World"
print(f"The sum of {num1} and {num2} is: {add_numbers(num1, num2)}")
print(add_space_to_strings(str1, str2))
