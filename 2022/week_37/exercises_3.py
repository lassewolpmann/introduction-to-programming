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

sentence_one = sentence_one.replace(',', '')
sentence_one = sentence_one.replace("'", '')
print(sentence_one)

'''
3. Find the index of the second article ‘the’ from the following sentence using a suitable string method.
’Turku is a city and former capital on the southwest coast of Finland at the mouth of the Aura River’
'''
sentence_two = "Turku is a city and former capital on the southwest coast of Finland at the mouth of the Aura River"
print(sentence_two.find('the', sentence_two.find('the') + 1))

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
print(stars_outline)
print(f'* {word_two} *')
print(stars_outline)
