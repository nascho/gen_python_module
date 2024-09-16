# 1
# rental car

"""
answer = input('What car would you like to rent today?\n')
print(f'Let me just check our database for the {answer.title()} you would like to rent.')

print('\n/*******************************************************************/\n')
"""

# 2
# dinner guests invited

"""
dinner_guests = int(input('How many people are in your dinner group?\n'))

if dinner_guests > 8:
  print("You'll need to wait for a table.")
else:
  print("Your table is ready.")
"""

# 3
# number is multiple of ten

"""
number = int(input("Give me a number:\n"))

if number % 10 == 0:
  print('That is a multiple of ten.')
else:
  print('Not a multiple of ten.')
"""

# 4
# pizza toppings

"""
print("Type 'quit' to exit the loop.")
pizza_topping = input("Name your pizza topping?\n").lower()
toppings = []

while pizza_topping != 'quit':
  toppings.append(pizza_topping.title())
  print(f"You have added {pizza_topping.title()}")
  print(f"Your pizza has the following toppings: {toppings}")
  pizza_topping = input("Name your pizza topping?\n").lower()
"""

# 5
# ticket prices

"""
print("Type 'quit' to exit the loop.")
age = input("How old are you?\n").lower()

while age != "quit":
    try:
        age = int(age)  # Convert the input to an integer for comparison
        if age < 3:
            print("Under 3's are free")
        elif 3 <= age <= 12:
            print("The ticket price is: $10")
        elif age > 12:
            print("The ticket price is: $15")
        break  # Exit the loop after providing the price
    except ValueError:
        print("Please enter a valid age.")
    
    # Ask for the next age or to quit
    age = input("How old are you?\n").lower()
"""

# 6
# no to infinite loop