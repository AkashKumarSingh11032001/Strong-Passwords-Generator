import random

num_pass = eval(input("Number of Password you want to create: "))
len_pass = eval(input("Length of each Password: "))

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

print("Your Password: ")

for i in range(num_pass):
    password = ''
    for j in range(len_pass):
        password += random.choice(chars)
    print(password)
