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

print("\n/*************************************************************/\n")

# 3
# car 

class Car():

  def __init__(self, make, model, year, mileage):
    self.make = make
    self.model = model
    self.year = year
    self.mileage = mileage

  def get_info(self):
    return (f"Make: {self.make.title()}\nModel: {self.model.title()}\nYear: {self.year}\nMileage: {self.mileage}\n")

  def set_mileage(self, miles):
    self.mileage = miles

  def get_mileage(self):
    return self.mileage

car_1 = Car('ford', 'focus', 2012, 130000)
car_2 = Car('mercades benz', 'g-class', 2022, 50000)
car_3 = Car('porsche', '911', 2018, 8000)

print(car_1.get_info())
print(car_2.get_info())
print(car_3.get_info())

car_3.set_mileage(8041)
print(car_3.get_mileage())
car_3.set_mileage(0)
print(car_3.get_mileage())
car_3.set_mileage(8059)
print(car_3.get_mileage())

print("\n/*************************************************************/\n")

# 4
# books

class Book():
  
  def __init__(self, author, title, genre, pages):
    
    self.author = author
    self.title = title
    self.genre = genre
    self.pages = pages

  def display_info(self):
    return f"{self.title.title()} is based on {self.genre.title()} written by {self.author.title()}."
  
  def set_pages(self, num_of_pages):
    self.pages = num_of_pages

  def get_pages(self):
    return f"{self.pages} pages"
  
book_1 = Book('jospeh heller', 'catch-22', 'dark comedy', '200')
book_2 = Book('robert greene', '48 rules of power', 'self help', '150')

print(book_1.display_info())
print(book_2.display_info())

print(book_2.get_pages())
book_2.set_pages(198)
print(book_2.get_pages())

print("\n/*************************************************************/\n")

# 5
# bank account

class BankAccount():
  
  def __init__(self, acc_num, acc_holder, bal):
    self.acc_num = acc_num
    self.acc_holder = acc_holder
    self.bal = int(bal)

  def deposit(self, amount):
    print(f"Previous balance was: {self.bal}")
    self.bal += int(amount)
    print(f"New balance including deposit: {self.bal}")

  def withdrawal(self, amount):
    if self.bal > amount:
      print(f"Currect balance: {self.bal}")
      self.bal -= amount
      print(f"New balance: {self.bal}")
    else:
      print(f"Insufficient balance to make a withdrawal of: {amount}")

  def get_statement(self):
    return f"{self.acc_holder.title()} your account number is: {self.acc_num} and your balance is: {self.bal}."

customer_1 = BankAccount('12345', 'adam smith', 0)
print(customer_1.get_statement())

customer_1.deposit(100)
customer_1.withdrawal(50)
print(customer_1.get_statement())