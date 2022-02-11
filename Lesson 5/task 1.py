import random
random_number = random.randint(1, 10)
number = int(input('Input number between 1 and 10: '))
while number != random_number:
    if number < random_number:
        number = int(input('Your number is less, input another number '))
    elif number > random_number:
        number = int(input('Your number is higher, input another number '))
print('Ok, you guessed the number')