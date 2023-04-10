def write_file_content():
    current_name = input("enter Hebrew content:\n")
    file = open("hebrew_file.txt", "w")
    file.write(f"{current_name}\n")
    file.close()


def print_file_content():
    file = open("hebrew_file.txt", "r")
    for line in file.readlines():
        print(f"{line}", end='')
    file.close()


write_file_content()
print_file_content()