global_variable = 'This is a global variable'


def task_1():
    # What are the differences between global, local and nonlocal variables?
    local_variable = 'This is a local variable'

    def make_non_local():
        nonlocal local_variable
        local_variable = 'This is now a non-local variable'

    print(global_variable)
    print(local_variable)
    make_non_local()
    print(local_variable)

    # In which cases would you use a global variables? Give some practical examples
    # Global variables are usually used for data like API keys, URLs etc.
    # For example:
    API_KEY = 'abcdef'


def task_2():
    try:
        print('Press ENTER to start')
        whitespace = 0
        while True:
            for i in range(6):
                if input() == '':
                    print('o'.rjust(whitespace + 1), end='')

                    if 0 <= i % 6 < 3:
                        whitespace += 1

                    elif 3 <= i % 6 < 6:
                        whitespace -= 1

                else:
                    print('Input other than ENTER detected. Exiting program!')
                    raise StopIteration

    except StopIteration:
        pass


def task_3():
    print('Press ENTER to start')

    o_whitespace = 0
    x_whitespace = 0

    while True:
        if o_whitespace < 12:
            o_string = 'o'.rjust(o_whitespace + 1)
            print(o_string, end='')
            o_whitespace += 1

        else:
            x_string = 'x'.rjust(x_whitespace + 1)
            print(x_string, end='')
            x_whitespace += 2

            o_string = 'o'.rjust(o_whitespace + 1 - len(x_string))
            print(o_string, end='')
            o_whitespace += 1

            if o_whitespace + 1 - len(x_string) == 2:
                print('\n')
                print('Game over! x reached o.')
                break

        input()


def task_4():
    import random
    import string

    alphabet = []
    vowels = []
    consonants = []
    word_list = []

    for letter in string.ascii_letters:
        if letter.lower() in ['a', 'e', 'i', 'o', 'u', 'y']:
            vowels.append(letter)

        else:
            consonants.append(letter)

        alphabet.append(letter)

    for i in range(int(input('How many words do you want?: '))):
        # word is 5 or 7 characters long randomly
        word_length = random.choice([5, 7])

        # each word starts with a random consonant and the second letter is always a random vowel
        random_word = f'{random.choice(consonants)}{random.choice(vowels)}{"".join(random.choices(alphabet, k=2))}'

        if word_length == 5:
            # any word with the length of 5 will end in a random vowel
            random_word = f'{random_word}{random.choice(vowels)}'

        elif word_length == 7:
            # two last letters of word with length of 7 will not both be vowels nor consonants
            if random.randint(1, 2) == 1:
                random_word = f'{random_word}{random.choice(alphabet)}{random.choice(vowels)}{random.choice(consonants)}'

            else:
                random_word = f'{random_word}{random.choice(alphabet)}{random.choice(consonants)}{random.choice(vowels)}'

        word_list.append(random_word)

    print(word_list)


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
