sum_of_number = 0
digit_counter = 0
while digit_counter < 100:
    if digit_counter % 3 == 0 and digit_counter % 5 == 0 :
        sum_of_number = sum_of_number + digit_counter
    digit_counter += 1
print(sum_of_number)
