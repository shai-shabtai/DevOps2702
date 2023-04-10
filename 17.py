def add_name_to_file():
    name = input("Please enter a name:\n")
    names_file = open("names.txt", "w")
    names_file.write(name)


def read_names_from_file():
    names_file = open("names.txt")
    for line in names_file.readlines():
        print(f"Hello {line}\n")


add_name_to_file()
read_names_from_file()
