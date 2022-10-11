def task_1():
    # 1
    # Some countries measure temperature in Fahrenheit degrees.
    # The conversion formula between Celsius and Fahrenheit scales is
    # c / 5 = (f -32) / 9
    # Your task is to design a code that asks three integer variables start, end and step.
    # The program prints a table where the first column contains the degrees in Fahrenheit
    # and the second column has degrees in Celsius.
    # The rows begin from start to end with increments step in Fahrenheit scale.
    # In addition, start and end are included.
    # Expected output:
    # Give a start degree in F:80
    # Give an end degree in F:100
    # Give a step degree in F:3
    # F     C
    # --------------------
    # 80    26.7
    # 83    28.3
    # 86    30.0
    # 89    31.7
    # 92    33.3
    # 95    35.0
    # 98    36.7
    start_value = int(input('Give a start degree in F: '))
    end_value = int(input('Give an end degree in F: '))
    step_value = int(input('Give a step degree in F: '))

    print('F\t\tC')
    print('--------------------')
    for f in range(start_value, end_value, step_value):
        c = ((f - 32) * 5) / 9
        print(f'{f}\t\t{round(c, 1)}')


def task_2():
    # 2
    # Again we utilize randrange() function to roll a die.
    # Task: Roll a die until you will get 6. However, roll max 5 times.
    # Expected output:
    # Rolling: 3 5 1 6
    # or
    # Rolling: 6
    # or
    # Rolling: 5 1 2 4 2
    # Hint: There are several ways to code the exercise. Think over the keywords told at the beginning of the exercises.
    import random

    roll_list = []
    while True:
        r_int = random.randrange(1, 7)
        roll_list.append(r_int)
        if r_int == 6 or len(roll_list) >= 5:
            break

        else:
            continue

    print(f'Rolling: {" ".join(map(str, roll_list))}')


def task_3():
    # 3
    # Retrieved from the currency exchange rates table https://www.x-rates.com/table/?from=EUR&amount=1
    # Oct 09, 2022 08:58 UTC
    # we can see that
    # 1 euro = 0.974015 US Dollar
    # 1 euro = 0.878185 British Pound
    # 1 euro = 6.929159 Chinese Yuan Renminbi
    # Write a program that asks first ‘How many euros?’
    # and calculates and prints the amount in three different currencies according to the table.
    # The program asks in the end: ‘Do you want to continue?’
    # You can answer ‘y’ or ‘n’.
    # If your answer is ‘y’, the program goes to the beginning, and you can continue as far as you want.
    # The program ends when your answer is ‘n’.
    # If you answered something else, the message ‘You did not answer y or n’ is displayed and the program continues
    # from the beginning.

    while True:
        eur_value = float(input('How many euros?: '))

        print(f'{eur_value} euro(s) = {eur_value * 0.974015} US Dollar')
        print(f'{eur_value} euro(s) = {eur_value * 0.878185} British Pound')
        print(f'{eur_value} euro(s) = {eur_value * 6.929159} Chinese Yuan Renminbi')

        choice = input('Do you want to continue?: ')
        if choice == 'n':
            break

        elif choice == 'y':
            continue

        else:
            print('You did not answer y or n')
            continue


def task_4():
    # 4
    # It is possible to pause the running program (so-called thread)
    # with the function sleep() that is in the module named time.
    # The pause can be n (positive integer) seconds.
    # How do you code a program that asks the variable start (the positive integer)
    # and then counts down starting from start?
    # The program prints the numbers from start to one (including both).
    # Each number is pausing at one second. In this exercise while loop is required.
    # Expected output. The text in parentheses may be printed or not:
    # Give a starting integer:6
    # 6     (pause 1 second)
    # 5     (pause 1 second)
    # 4     (pause 1 second)
    # 3     (pause 1 second)
    # 2     (pause 1 second)
    # 1     (pause 1 second)
    # Boom!

    import time

    start_value = int(input('Give a starting integer: '))
    while start_value > 0:
        print(f'{start_value}\t\t(pause 1 second)')
        start_value -= 1
        time.sleep(1)

    print('Boom!')


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
