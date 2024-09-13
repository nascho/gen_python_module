# 1
# create a dictionary

person = {
  'first_name': 'Hello',
  'last_name': 'World',
  'age': 30,
  'city': 'London'
}

print(person)

print('/****************************************************/')

# 2
# create favourite number dictionary

favourite_numbers = {
  'adam': 1,
  'ben': 2,
  'charlie': 3,
  'dean': 4,
  'eric': 5
}

for k, v in favourite_numbers.items():
  print(f'Hello, my name is {k.title()} and my favourite number is {v}.')

print('/****************************************************/')

# 3
# rivers and countries

rivers_countries = {
  'nile': 'egypt',
  'thames': 'united kingdom',
  'amazon': 'brazil'
}

for k, v in rivers_countries.items():
  print(f'The {k.title()} runs through {v.title()}.')

for river in rivers_countries.keys():
  print(f'The name of the river is {river.title()}.')

for country in rivers_countries.values():
  print(f'The name of the country is {country.title()}.')

print('/****************************************************/')

# 4
# list with several dictionaires

mr_dog = {
  'animal': 'dog',
  'owner': 'adam'
}

mr_cat = {
  'animal': 'cat',
  'owner': 'ben'
}

pets = [mr_dog, mr_cat]
print(pets)

for x in pets:
  print(x)

for x in pets:
  print(x.keys())

for x in pets:
  print(x.values())

for pet in pets:
  print(f"Hello, I am a {pet['animal']} and my owner is {pet['owner'].title()}.")

print('/****************************************************/')

# 5
# favourite_places

favourite_places = {
  'adam': 'london',
  'ben': 'yorkshire',
  'clive': 'not croydon'
}

for k,v in favourite_places.items():
  print(f"{k.title()} has a favourite place and it is: {v.title()}.")

print('/****************************************************/')

# 6
# dictionary about cities

cities = {
  'london': {
    'country': 'united kingdom',
    'population': '70 million',
    'fact': 'there\'s a secret undergrand mail train, you can ride'
  },
  'paris': {
    'country': 'france',
    'population': '68 million',
    'fact': 'called the city of light'
  },
  'berlin': {
    'country': 'united kingdom',
    'population': '84 million',
    'fact': '9 times bigger than Paris'
  }
}

print(cities)

for city, data in cities.items():
  print(f"\nCity: {city.title()}")
  for k, v in data.items():
    print(f"{k.title()}: {v.title()}")

print('/****************************************************/')

