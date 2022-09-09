# Exercises 2
print('Exercises 2')
'''
1. You have a string s = ‘Python is a good language’
Use slices and + to construct the string ‘Python is a language’ from s
'''
s = 'Python is a good language'
print(s[:11] + s[16:])

'''
2. Use input function to ask ‘Type here a word’. Print so many stars  as the word has characters.
For example, you wrote the word ‘leopard’ and your code prints *******
'''
word = input('Type here a word: ')
stars = len(word) * '*'
print(stars)

'''
3. Slice and indexing work with lists too. Apply input function to ask three floats from the user.
Add every word to a list using append function. This function works so that if the name of the list is  lst, 
lst.append(10) adds 10 to the list lst.
Finally print a new list which contains two first words from lst.
'''
number_list = []
number_list.append(float(input('Number 1: ')))
number_list.append(float(input('Number 2: ')))
number_list.append(float(input('Number 3: ')))

print(number_list[:2])

'''
number_list = []

for i in range(1000):
    number_list.append(float(input(f'Number {i + 1}: ')))
    
print(number_list[:2])


number_list = [float(input('Number 1: ')), float(input('Number 2: ')), float(input('Number 3: '))]
print(number_list[:2])
'''

'''
4. Use a tuple to assign x = 3, y = 8 and z = 4.
With the help of x, y and z write the code which prints the tuple (4, 3, 8, 15). 15 = 4+3+8.
'''
number_tuple = (3, 8, 4)
x = number_tuple[0]
y = number_tuple[1]
z = number_tuple[2]
print((z, x, y, x + y + z))
