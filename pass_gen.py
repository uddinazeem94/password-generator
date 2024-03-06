# PyPassword Generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters do you want in your Password?\n>>"))
nr_numbers = int(input("How many numbers would you like?\n>>"))
nr_symbols = int(input("How many symbols\n>>"))

password = []
for letter in range(0,nr_letters + 1):
    random_l = random.randint(0,51)
    password += letters[random_l]
for number in range(0, nr_numbers+1):
    random_n = random.randint(0,9)
    password += numbers[random_n]
for symbol in range(0,nr_symbols+1):
    random_s = random.randint(0,8)
    password += symbols[random_s]

random.shuffle(password)
pass_redef = ''
for each in password:
    pass_redef += each
print(pass_redef)