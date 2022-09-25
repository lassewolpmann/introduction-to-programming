# Exercises 4
print('Exercises 4')


def task_1():
    # Task 1
    print('Task 1')
    '''
    a) Convert the string "15.5" into integers. Try to do this directly from the given string first.
    Afterward convert the string first to a float and then from float to an int. Explain why this happens.
    '''
    n_str = '15.5'

    # String -> Int
    try:
        print(int(n_str))

    except ValueError as Error:
        print(Error)

    # String -> Float -> Int
    print(int(float(n_str)))

    '''
    b) Convert the boolean value True into string. 
    Now convert the boolean value first to integer and then from integer to string.
    '''
    b_value = True

    # Bool -> String
    print(str(b_value))

    # Bool -> Int -> String
    print(str(int(b_value)))

    '''
    c) Convert the floating point value 1.1 into integers. 
    Convert the resulting integer back into floating points.
    '''
    f_value = 1.1

    # Float -> Int -> Float
    print(float(int(f_value)))

    '''
    d) Convert the string "Esther” into a list. Convert that list back to a string. Print the string onscreen. 
    Then print the first index of that string on screen.
    '''
    s = 'Esther'

    # String -> List
    print(list(s))

    # String -> List -> String and printing first index
    print(str(list(s))[0])

    '''
    e) As a conclusion from a)-d), what can you say about invertibility of type conversions?
    
    After a value has been converted, it is not possible to easily go back it's original type.
    '''


def task_2():
    # Task 2
    print('Task 2')

    '''
    Implement a program that asks the user for three numbers. 
    The program calculates and prints the mean value and average absolute deviation of the given numbers. 
    We'll be using the Python built-in function abs() here. 
    abs() returns the absolute value of a number given as its parameter. So, for example abs(-3) would return 3.
    You can use the following formulas for the calculations:
    Mean value of numbers x1, x2 and x3: mean_value = (x1 + x2 + x3) / 3
    Absolute deviation of number x1: abs_dev_x1 = abs(x1 - mean_value)
    Average absolute deviation: avg_abs_dev = (abs_dev_x1 + abs_dev_x2 + abs_dev_x3) / 3
    
    Expected output:
    Give value for x1: 10.1
    Give value for x2: 11.1
    Give value for x3: 12.1
    
    Mean value: 11.1
    Absolute deviation of x1: 1.0
    Absolute deviation of x2: 0.0
    Absolute deviation of x3: 1.0
    Average absolute deviation: 0.666666666666
    
    When programming, it's important to think about possible edge cases. 
    What kind of input causes your program to throw an exception and fail? Give an example. Why does this happen?
    '''
    numbers = []
    for i in range(3):
        while True:
            try:
                n_input = float(input(f'Enter Number {i + 1}: '))
                numbers.append(n_input)

                break

            # Do not accept any input, that can't be converted to float
            except ValueError:
                print('Invalid input, try again!')

    mean_value = sum(numbers) / len(numbers)

    abs_dev = []
    for n in numbers:
        abs_dev.append(abs(n - mean_value))

    avg_abs_dev = sum(abs_dev) / len(abs_dev)

    print(f'Mean value: {mean_value}')

    for x, dev in enumerate(abs_dev):
        print(f'Absolute deviation of x{x + 1}: {dev}')

    print(f'Average absolute deviation: {avg_abs_dev}')


def task_3():
    # Task 3
    print('Task 3')

    '''
    Given a random floating point number num_a, 
    form a floating point number num_b such that its integer part is num_a's fractional part
    and its fractional part is num_a's integer part.
    
    That is:
    if
    num_a = 11.22
    then
    num_b = 22.11
    
    Generate the random floating point number with the following code snippet. 
    It will generate numbers from 0 to 99.99 and round those to two decimal precision:
    import random
    num_a = round(random.uniform(0, 99.99), 2)
    Expected output:
    Generated random floating point value: 11.3
    Modified number with swapped integer and fractional parts: 3.11
    
    Hint:
    There are a multitude of different ways to solve this. You could use at least type conversions,
    string method split(),
    string slicing,
    and modulo operator for help in getting the pieces separated and back together. 
    
    Some of these routes are considerably more difficult than the others. Try them out!
    '''
    import random

    # Way 1
    num_a_1 = round(random.uniform(0, 99.99), 2)
    print(num_a_1)

    num_b_1 = f'{str(num_a_1).split(".")[1]}.{str(num_a_1).split(".")[0]}'
    print(num_b_1)

    # Way 2
    num_a_2 = round(random.uniform(0, 99.99), 2)
    print(num_a_2)

    n1 = str(round(num_a_2 % 1 * 100)).rjust(2, "0")    # Make sure to have a leading 0, if number < 10
    num_b_2 = f'{n1}.{int(num_a_2)}'
    print(num_b_2)


def task_4():
    # Task 4
    print('Task 4')

    '''
    Implement a program that asks the user for the number of enrolled students on a course 
    and the maximum amount of students per lab group.
    The program then calculates the minimum number of lab groups that are needed to fulfil the given constraints. 
    Try to solve this without conditional statements 
    (that is, do not use "if" -statements which we have not discussed on lectures yet).
    
    Expected output:
    How many students have enrolled on the course? 100
    What's the maximum number of students per lab group? 30
    The minimum number of lab groups needed with these constraints: 4
    
    Hint:
    The challenge here arises when the students cannot be evenly divided into groups
    and we are not allowed to use conditional statements. 
    It gets difficult to get both situations correct at the same time. 
    Why does rounding up solve this issue?
    We have learnt that integer division (denominator // numerator) always rounds down. 
    If however we wanted to round the result up, we could use the following formula:
    (numerator + denominator - 1) // denominator
    '''
    students = int(input('How many students have enrolled on the course?: '))
    max_per_lab = int(input("What's the maximum number of students per lab group?: "))

    min_lab_groups_1 = (students + max_per_lab - 1) // max_per_lab
    print(f'The minimum number of lab groups needed with these constraints: {min_lab_groups_1}')

    # or
    import math
    min_lab_groups_2 = math.ceil(students / max_per_lab)
    print(f'The minimum number of lab groups needed with these constraints: {min_lab_groups_2}')


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
