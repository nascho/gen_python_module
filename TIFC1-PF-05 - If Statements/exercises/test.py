# 1
word = 'apple'

if word == 'apple':
  print(f'yes the word is: {word}.')

if word != 'orange':
  print(f'{word} is not part of the word selected')

print('/*******************************************************/')

# 2
age = 2

if age < 2:
  print('baby')
elif age < 4:
  print('toddler')
elif age < 13:
  print('kid')
elif age < 20:
  print('teenager')
elif age < 65:
  print('adult')
elif age >= 65:
  print('older')
else:
  print('error')

print('/*******************************************************/')

# 3
favourite_fruits = ['apple', 'banana', 'orange', 'pear']

for fruit in favourite_fruits:
  if fruit in favourite_fruits:
    print(f'You must really like {fruit}.')
  elif fruit in favourite_fruits:
    print(f'You must really like {fruit}.')
  elif fruit in favourite_fruits:
    print(f'You must really like {fruit}.')
  elif fruit in favourite_fruits:
    print(f'You must really like {fruit}.')
  else:
    print('error')

print('/*******************************************************/')

# 4
usernames = ['admin', 'ben', 'charles', 'dean', 'eric']

for name in usernames:
  if name == 'admin':
    print(f'Hello {name}, would you like to see a status report?')
  else:
    print(f'Hi {name.title()}, you have logged in.')

