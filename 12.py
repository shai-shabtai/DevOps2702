my_items = [{"name": "aviel", "age": 33}, {"name": "moshe", "age": 20},
            {"name": "david", "age": 50}]
aa = [item["name"] for item in my_items if item["age"] > 30]
print(aa)