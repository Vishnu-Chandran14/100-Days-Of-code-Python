#import random for randomazitation

import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#welocme on board and ask the user input

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy level password generator - password wil be generatored in the followiung orders letters, symbols, numbers  

sample = ""
for char in range(0, nr_letters):
  no_of_letters = random.choice(letters)
  sample = sample + no_of_letters
for char in range(0, nr_symbols):
  no_of_symbols = random.choice(symbols)
  sample = sample + no_of_letters
for char in range(0, nr_numbers):
  no_of_numbers = random.choice(numbers)
  sample = sample + no_of_numbers
  
print(sample)

#Hard level password generator - password will be generatored in the mixed orders with letters, symbols, numbers

password_list = []
for char in range(0, nr_letters):
  no_of_letters = random.choice(letters)
  password_list.append(no_of_letters)

for char in range(0, nr_symbols):
  no_of_symbols = random.choice(symbols)
  password_list.append(no_of_symbols)

for char in range(0, nr_numbers):
  no_of_numbers = random.choice(numbers)
  password_list.append(no_of_numbers)

print(password_list)

#shuffled the password

random.shuffle(password_list)
print(password_list)


#print the password in text format not list
password = ""
for i in password_list:
  password = password + i

print(f"Your password is : {password}")


