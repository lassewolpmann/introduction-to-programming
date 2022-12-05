def task_1():
    # Read the text file and print all unique words
    with open('text_files/goodMorning.txt') as file:
        text = file.read()

        for word in text.split():
            if word.isalpha():
                print(word)


def task_2():
    # Read the text file line by line using readline().
    # Print only the lines that contain at least one number character.

    with open('text_files/goodMorning.txt') as file:
        data = file.read()
        for line in data.split('\n'):
            if any(char.isdigit() for char in line):
                print(line)


def task_3(filename):
    with open(f'text_files/{filename}', 'w') as file:
        while True:
            word = input('Give word (write "end" to stop program): ')

            if word == 'end':
                break

            else:
                file.write(f'{word}\n')


def task_4():
    with open('text_files/dictionary.txt') as file:
        dictionary = file.readlines()
        word_dict = {line.split()[0]: line.split()[1] for line in dictionary}

        correct_guesses = 0
        for finnish_word in word_dict:
            english_word = word_dict.get(finnish_word)
            if input(f'What is the english word for {finnish_word}: ') == english_word:
                correct_guesses += 1

        print(f'You guessed {correct_guesses} translations correct!')


if __name__ == '__main__':
    task_1()
    task_2()
    task_3('test.txt')
    task_4()
