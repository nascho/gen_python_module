# 1 
# print out a for loop of pizzas

pizzas = ['pepperoni', 'all the meats', 'vegetarian']

for pizza in pizzas:
  print(pizza)
  print(f'----- I like to eat {pizza} pizza.')

print('----- I like to eat pizza with fried chicken -----')

print('/****************************************************************/')

# 2
# print out a list of animals

animals = ['dog', 'cat', 'horse']

for animal in animals:
  print(animal)
  print(f'A {animal} would make a good pet and teach you some resposibility.')

print('All of these animals are 4 legged - that\'s what they have in common.')

print('/****************************************************************/')

# 3
# print a  range of numbers

for num in range(1, 21):
  print('Hello, I\'m the number: ' + str(num))

print('/****************************************************************/')

# 4
# using min, max, sum

num_functions = (1, 1000000)
print(min(num_functions))
print(max(num_functions))
print(sum(num_functions))

print('/****************************************************************/')

# 5
# multiples of three

multiples_of_three = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

for num in multiples_of_three:
  print(num)

for num in multiples_of_three:
  print(num * 3)

print('/****************************************************************/')