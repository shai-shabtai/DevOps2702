## Option 1
x_length = 7
y = 9
for i in range(1, x_length + 1):
    x = ""
    for j in range(1, x_length + 1):
        if i == j or i == (x_length -j +1):
            x = x + "*"
        else:
            x = x + " "
    print(x)
print("\n")

## Option 2
x_length = 7
for i in range(1, x_length + 1):
    x = ""
    for j in range(x_length, 0, -1):
        if i == j or i == (x_length -j +1):
            x = x + "*"
        else:
            x = x + " "
    print(x)
