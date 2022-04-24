# Password Generator Project
import random
import string

# Gets length of desired password from user.
print("Welcome to the PyPassword Generator!")
length = int(input("Enter length of password you want? "))
# Data to be randomized.
nr_letters = string.ascii_letters
nr_symbols = string.punctuation
nr_numbers = string.digits

# Combines all the data and randomizes it and prints it out.
total = nr_letters + nr_symbols + nr_numbers
temp = random.sample(total, length)
password = "".join(temp)
print(password)
