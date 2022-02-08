string_to_truncate = 'I have a beautiful cat!'
len_string = len(string_to_truncate)
while len_string > 1:
    new_string = string_to_truncate[:(len_string - 1)]
    len_string -= 1
    print(new_string)
print("Nothing's left here")
