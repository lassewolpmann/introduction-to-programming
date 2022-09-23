# Exercises 1
print('Exercises 1')

'''
1. The program asks a word. Then the program prints first the stars and then the word. 
The total number of characters should be 15. 
For example, if you typed the word school, the program prints the line *********school
'''
word_one = input('Enter a word: ')
print(word_one.rjust(15, '*'))

'''
2. ‘Prince Edward, the Queen's youngest son, 
and his wife Countess Sophie published a statement thanking Queen Elizabeth II for her years of service.’

The text above should be printed so that there are no commas and no ’s 
'''
sentence_one = "Prince Edward, the Queen's youngest son, and his wife Countess Sophie published a statement " \
               "thanking Queen Elizabeth II for her years of service."

for ch in [",", "'"]:
    sentence_one = sentence_one.replace(ch, '')

print(sentence_one)

'''
3. Find the index of the second article ‘the’ from the following sentence using a suitable string method.
’Turku is a city and former capital on the southwest coast of Finland at the mouth of the Aura River’
'''
sentence_two = 'Turku is a city and former capital on the southwest coast of Finland at the mouth of the Aura River'

word_to_look_for = 'the'
word_length = len(word_to_look_for)
word_occurrence = sentence_two.count(word_to_look_for)
wanted_word_index = 2   # starting at 0, 1 means the second 'the' in this case

find_index = 0
for i in range(word_occurrence):
    word_index = sentence_two.find(word_to_look_for, find_index)
    print(word_index)
    if i == wanted_word_index:
        print(f'{wanted_word_index + 1}. "{word_to_look_for}" is at index {word_index} to {word_index + word_length}')

    else:
        find_index = word_index + 1

'''
4. The program asks a word. If, for example, the word ‘elephant’ is written, 
the program prints a frame outside the text. 
The frame changes according to the word.

************
* elephant *
************
'''
word_two = input('Enter a word: ')
stars_outline = (len(word_two) + 4) * '*'
print(f'{stars_outline}\n* {word_two} *\n{stars_outline}')
