def city_coutry(city, country):
    city_and_country = f"{city}, {country}."
    return city_and_country.title()


message = city_coutry('paris', 'france')
print(message)

message = city_coutry('brussels', country='belgium')
print(message)

message = city_coutry(city='chania', country='greece')
print(message)
