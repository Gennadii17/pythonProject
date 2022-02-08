len_name = len('Zharkov')
digit_counter = 1
factorial = 1
while digit_counter <= len_name:
    factorial = factorial * digit_counter
    digit_counter += 1
print(str(len_name) + '! = ' + str(factorial))
