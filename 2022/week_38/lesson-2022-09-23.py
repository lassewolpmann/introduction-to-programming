# SHORTENED VERSIONS OF ASSIGNMENT OPERATORS
a = 3
print(a + 1)
print(a)    # Value of "a" remains 3
a = a + 1   # Value of "a" is now a + 1
a += 1      # Same calculation but in a shorter way
print(a)    # Value of "a" is now 5

# This showcases why += is better and cleaner to write
very_long_variable_name = 10
very_long_variable_name = very_long_variable_name + 5
very_long_variable_name += 5
very_long_variable_name -= 10
print(very_long_variable_name)

# CONDITIONAL STATEMENTS
x = int(input('Give an integer: '))
if x > 0:
    print('x is positive')  # This line only gets executed when x is bigger than 0

elif x < 0:
    print('x is negative')

elif x <= 0:
    print('x is negative or 0')

elif x >= 0:
    print('x is positive or 0')

else:
    print('this shouldnt happen')

name = input('Your name: ')
q1 = input('Do you want to continue? (y/n): ')

if q1 == 'y':
    age = int(input('Tell me your age: '))
    print(f'Your name is {name} and you are {age} years old.')

else:
    print(f'Your name is {name}, but I do not know your age.')

# Multiple branches
temperature = float(input('What is the temperature right now?: '))

if temperature > 0:
    print('It is over 0 °C')

elif temperature == 0:
    print('It is exactly 0 °C')

elif temperature == 4:          # This would not be executed since the first if-statement would end the block
    print('It is exactly 4 °C')

elif temperature == -4:
    print('It is exactly -4 °C')

else:
    print('It is under 0 °C')
