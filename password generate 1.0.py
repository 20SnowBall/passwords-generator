import random

password = []
print('1.0')
arg = '0123456789qwertyuiop[]asdfghjkl;zxcvbnm,./QWERTYUIOPASDFGHJKLZXCVBNM<>":}{@##$%^*!:}{@##$%^*!:}{----++++'
n = int(input('Enter the desired number of characters for the password: '))
for i in range(n):
    password.append(arg[random.randint(0, len(arg)-1)])
    print(password[i], end='')
print('')
print('Press enter to close')
close = input()