import random

password = []
print('1.1')
arg = '0123456789qwertyuiop[]asdfghjkl;zxcvbnm,./QWERTYUIOPASDFGHJKLZXCVBNM<>":}{@##$%^*!:}{@##$%^*!:}{----++++'

def otvet_f():
    print('1. Change the length')
    print('2. Skip')
    otvet = int(input())
    if otvet == 1:
        line()
    elif otvet == 2:
        False
    else:
        otvet_f()

def line():
    num = int(input('Enter the desired number of characters for the password: '))
    if num < 8:
        print('WARNING! This character length is too small and may not be safe!')
        otvet_f()
    else:
        False
        
while True:
    num = int(input('Enter the desired number of characters for the password: '))
    if num < 8:
        print('WARNING! This character length is too small and may not be safe!')
        otvet_f()
        break
    else:
        break

for i in range(num):
    password.append(arg[random.randint(0, len(arg)-1)])
    print(password[i], end='')
print('')
print('Press enter to close')
close = input()