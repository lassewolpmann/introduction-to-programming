# MULTILINE STRINGS

multiline_string = '''this
is
a
multiline
string'''

print(multiline_string)


# FORMATTING STRINGS (F-STRINGS)
txt = 'This calculation gives'
x = 5
y = 2.5318

# version 1
print(txt + ' ' + str(x + y))

# version 2
print(txt, x + y)

# best version
print(f'{txt} {x + y:.3f}')  # ":.3f -> rounding to float with 3 decimal places", same as round(x + y, 3)
# same as
print(f'{txt} {round(x + y, 3)}')

# more examples
print(f'5 * 5 = {5 * 5}')
print(f'Output: {int(input("Input number: ")) * 2}')


# MORE ABOUT STRINGS
sentence = 'Täällä on lämmin'
new_sentence = sentence.replace('ä', 'a')
print(sentence)
print(new_sentence)

number_sequence = '1 2 3 4 5'
print(number_sequence.replace(' ', ''))

sentence_two = 'Here we are learning Python'
print(sentence_two.replace('we are', "we're"))
print(sentence_two.split())
print(len(sentence_two.split()))

date = '13.09.2022'
date_list = date.split('.')
print(date_list)
print('/'.join(date_list))
