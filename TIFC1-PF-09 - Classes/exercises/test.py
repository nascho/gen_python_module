# 1
# restaurant method

class Restaurant():
  
  def __init__(self, restaurant_name, cuisine_type) -> None:
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0

  def describe_resturant(self):
    return f"The restaurant is called {self.restaurant_name} and serves {self.cuisine_type}."

  def open_restaurant(self):
    return "Open for business"
  
  def set_number_served(self, num):
    self.number_served = num
    return self.number_served

  def increment_number_served(self):
    self.number_served += 1
    return self.number_served



restaurant_1 = Restaurant('mcdonalds', 'american fast food')
print(f"The restaurant name is: {restaurant_1.restaurant_name.title()}")
print(f"The food they serve is: {restaurant_1.cuisine_type.title()}")
print(restaurant_1.describe_resturant())
print(restaurant_1.open_restaurant())

print("\n/***************************************************************/\n")

restaurant_2 = Restaurant('nandos', 'chicken')
restaurant_3 = Restaurant('kfc', 'fried chicken')
restaurant_4 = Restaurant('pizza hut', 'pizza')

print(restaurant_2.describe_resturant())
print(restaurant_3.describe_resturant())
print(restaurant_4.describe_resturant())

print("\n/***************************************************************/\n")

restaurant_5 = Restaurant('burger king', 'amercan fast food')
print(restaurant_5.number_served)

restaurant_5.number_served = 1
print(restaurant_5.number_served)

print("\n/***************************************************************/\n")

print(restaurant_5.set_number_served(2))
print(restaurant_5.number_served)

print("\n/***************************************************************/\n")

print(restaurant_5.increment_number_served())
print(restaurant_5.increment_number_served())
print(restaurant_5.increment_number_served())
print(restaurant_5.increment_number_served())
print(restaurant_5.increment_number_served())

print("\n/***************************************************************/\n")

# 2
# user

class  User():
  
  def __init__(self, first_name, last_name, age, gender):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.gender = gender
    self.login_attempts = 0

  def describe_user(self):
    return f"Hello my name is {self.first_name.title()} {self.last_name.title()}, I am {self.age} years old and {self.gender}."
  
  def greet_user(self):
    return f"Hi, {self.first_name.title()}."
  
  def increment_login_attempts(self):
    self.login_attempts += 1

  def reset_login_attempts(self):
    self.login_attempts = 0
  


user_1 = User('adam', 'smith', 30, 'male')
user_2 = User('ben', 'jone', 25, 'male')
user_3 = User('claire', 'davenport', 19, 'female')

print(user_1.describe_user())
print(user_1.greet_user())
print(user_2.describe_user())
print(user_2.greet_user())
print(user_3.describe_user())
print(user_3.greet_user())

user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.increment_login_attempts()
print(user_1.login_attempts)

print("\n/***************************************************************/\n")

