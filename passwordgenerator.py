import random

def password_generator(length):
    chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
    password=''
    for _ in range (length):
        password+=chars[ random.randint(0, len(chars)-1)]

    return password

p1=password_generator(10)
print('Your password generated is "', p1,'"')
print('Length of your password is "',len(p1), '"')
print ("-"*70)
p2=password_generator(100)
print('Your password generated is "', p2, '"')
print('Lenght of your password is "',len(p2), '"')
