a = ["daniel", "shai", "roei"]
is_shmulik = "shmulik"
if a[0] == is_shmulik or a[1] == is_shmulik or a[2] == is_shmulik:
    print("Shmulik exists")
else:
    print("Smulik doesn't exists")

if "shmulik" in a:
    print("Shmulik exists")
else:
    print("Smulik doesn't exists")

first_array = []
second_array = [1, 2, 3]
if not first_array:
    print("first array has not items")
if second_array:
    print("second array has items")
if len(second_array) > 2:
    print("we have at least 3 items in second")

d = 5
g = 5
f = [1, 2, 3]
h = [1, 2, 3]
if d is g:
    print("d is g")
if f is h:
    print("f is h")
if type(d) is int:
    print("d is int")