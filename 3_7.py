def get_name():
    current_name = input("enter your name:\n")
    file = open("words.txt", "w")
    file.write(f"{current_name}\n")
    file.close()


def print_name():
    file = open("words.txt", "r")
    for line in file.readlines():
        print(f"Hello {line}", end='')
    file.close()


get_name()
print_name()
