a = int(input("enter number: "))
b = int(input("enter number: "))
result = 0
try:
    result = a / b
except BaseException as e:
    print("something went wrong")
    print(e.args)
print(result)