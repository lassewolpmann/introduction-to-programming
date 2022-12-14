# Exercises 2
print('Exercises 2')

'''
1. You have a string s = ‘Python is a good language’
Use slices and + to construct the string ‘Python is a language’ from s
'''
s = 'Python is a good language'
s_split = s.split(' ')
print(f'{s_split[0]} {s_split[1]} {s_split[2]} {s_split[4]}')

'''
2. Use input function to ask ‘Type here a word’. Print so many stars  as the word has characters.
For example, you wrote the word ‘leopard’ and your code prints *******
'''
word = input('Type here a word: ')
print(len(word) * '*')

'''
3. Slice and indexing work with lists too. Apply input function to ask three floats from the user.
Add every float to a list using append function. This function works so that if the name of the list is  lst, 
lst.append(10) adds 10 to the list lst.
Finally print a new list which contains two first float from lst.
'''
number_list = []

for i in range(3):
    number_list.append(float(input(f'Number {i + 1}: ')))
    
print(number_list[:2])

'''
4. Use a tuple to assign x = 3, y = 8 and z = 4.
With the help of x, y and z write the code which prints the tuple (4, 3, 8, 15). 15 = 4+3+8.
'''
x, y, z = (3, 8, 4)
new_tuple = (z, x, y, x + y + z)
print(new_tuple)
