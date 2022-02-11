import random
word = input('Enter word: ')
word_list = list(word)
random.shuffle(word_list)
print(''.join(word_list))
