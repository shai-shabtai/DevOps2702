persons = [{"age": 34, "last_name": "shabtai", "dollar_shekel_currency": 3.60, "flew_abroad": True, "apartment_num": "56"}]
for person in persons:
    print(f"The age is: {person['age']}")
    print(f"The first latter of the last_name is: {person['last_name'][0]}")
    print(f"The Dollar-Shekel currency is: {person['dollar_shekel_currency']}")
    print(f"Is He/She flow abroad: {person['flew_abroad']}")
    print(f"The apartment number is: {person['apartment_num']}\n")
    curr_adding_to_age = person['age']+person['dollar_shekel_currency']
    print(f"Adding the currency to the age value is: {curr_adding_to_age}")

