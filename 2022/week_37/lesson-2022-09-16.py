# STRING COMMANDS AND METHODS (method is a function inside a class)
# Normal function example
print(round(2.8, 0))   # round() is the function name, 2.8 is the first argument and 0 is the second argument

# Class method example
s1 = 'Friday'
print(s1.lower())      # s1 is an object, lower() is a method that has no arguments

# answer = input('Yes or No: ')   # Answer can be for example "Yes, yes, No, no ..."
answer = input('Yes or No: ').lower()     # Now, the only possible answers are "yes and no"
print(answer == 'yes')

# Some other string-methods
s = 'geeks for geeks'
print(s.find('for'))    # Finding the index where "for" starts
print(s.find('e'))      # Finding the index for the first "e"
print(s.rfind('e'))     # right-find method, finding the index for the last "e" (first from right to left)
print(s.find('e', 1))   # Find the first "e", starting the search on index 1
print(s.find('e', 2))   # Find the first "e", starting the search on index 2
print(s.find(' g'))     # Finding the index for the first " g", WITH the whitespace in front of the g


# TIME MODULE
import time
now = time.ctime()
current_date = now.split()
print(current_date)
current_time = current_date[3]
print(current_time)
hms = current_time.split(':')   # hms = hours minutes seconds
print(f'{hms[0]} hours {hms[1]} minutes and {hms[2]} seconds')


# BACK TO STRING METHODS
sentence = """Hello
Python
again
"""
print(sentence)
sentence_list = sentence.splitlines()   # Splitting the string at each newline
print(sentence_list[::-1])  # ::-1 to reverse list

s2 = 'great britain'
print(s2.title())   # Turns sentence into titlecase
print(s2.count('e'))    # Counts the amount of "e"

number_string = '753'
print(number_string.isalnum())  # Checks if string contains only alphanumerics (Alphabet and numbers)
letter_string = 'abc'
print(letter_string.isalpha())  # Check if string contains only alphabet

Bond = '7'.zfill(3)     # Fills string in the beginning with zeroes until given "width" is achieved
print(Bond)

whitespace_string = '       Test string with a lot of whitespaces      '
print(whitespace_string.strip())    # Removes all leading and trailing whitespaces

ans = input('Your ID: ').strip()    # Remove accidental whitespaces for "clean" input
print(ans)


# TRUE AND FALSE
# True can be expressed as number 1, and number 1 as True
print(type(True))
print(int(True))
print(bool(1))

# False can be expressed as number 0, and number 0 as False
print(type(False))
print(int(False))
print(bool(0))
