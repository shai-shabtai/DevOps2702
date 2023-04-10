names = ["inbar", "lanir", "eran", "kfir", "alina"]
print(list(range(2, 20, 2)))
for name in names:
    print(name)
for i in range(len(names)):
    print(names[i])

a = 0
while a < 5:
    print(a)
    a = a + 1
else:
    print("Finished successfully")

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    if number == 3:
        continue
    if number == 2:
        break
    print(number)
else:
    print("Finished successfully")

