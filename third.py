from first import get_number
from second import addition


def main():
    a = get_number()
    b = get_number()
    print(addition(a, b))


#main()

a = 0
for i in range(10):
    a = a + i
    print(a)