try:
    a = 1 / 0
except ZeroDivisionError:
    print("Error dividing by zero")
finally:
    print("finaly")