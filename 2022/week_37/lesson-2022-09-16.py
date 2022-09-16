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
