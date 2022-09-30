# Exercises 5
print('Exercises 5')


def task_1():
    # Task 1
    print('Task 1')
    '''
    # 1 In this exercise we'll practice forming conditional statements.
    That is, statements with a truth value. These are often used in if -statements and later on as conditions in loops.
    In this exercise however, you won't need to worry about any of that. Just form the conditions.
    Write a statement that assigns to variable x the truth value depending on the following condition:
    a) x is true, if the value of variable y is a vowel.
    b) x is true, if integer y is divisible by 7.
    c) x is always false
    d) x is true, if sum of variables a and b is either less than 20 or greater than 50
    '''

    # a)
    y = input('Give a letter of the alphabet: ')
    if y in ['a', 'e', 'i', 'o', 'u']:
        x = True

    else:
        x = False

    # b)
    y = int(input('Give an integer: '))
    if y % 7 == 0:
        x = True

    else:
        x = False

    # c)
    if True:
        x = False

    # d)
    a = float(input('Give any number for a: '))
    b = float(input('Give any number for b: '))

    if a + b < 20 or a + b > 50:
        x = True

    else:
        x = False


def task_2():
    # Task 2
    print('Task 2')
    '''
    #2 Write a program that asks the user for a number of points gained from solving programming exercises
    and outputs the grade according to the following chart:
    Points    Grade
    90-100    5
    80-89     4
    70-79     3
    60-69     2
    50-59     1
    0-50      Failed
    If the user gives a number of points that is not on the chart,
    the program outputs an error message about invalid input.
    
    Expected output:
    Enter the amount of exercise points: 50
    With 50 points your grade is: 1
    
    Enter the amount of exercise points: 79
    With 79 points your grade is: 3
    
    Enter the amount of exercise points: 110
    Points value out of range. Invalid input: 110
    '''

    points = int(input('Amount of points: '))

    if 100 >= points >= 90:
        grade = 5

    elif 89 >= points >= 80:
        grade = 4

    elif 79 >= points >= 70:
        grade = 3

    elif 69 >= points >= 60:
        grade = 2

    elif 59 >= points >= 50:
        grade = 1

    elif 49 >= points >= 0:
        grade = 'Failed'

    else:
        grade = None

    if grade:
        print(f'With {points} points, your grade is: {grade}')

    else:
        print(f'Points value out of range. Invalid input: {points}')


def task_3():
    # Task 3
    print('Task 3')
    '''
    #3 In this exercise we'll introduce the idea of a "guard" in conditional statements.
    The purpose of these guards is to protect the program from unexpected behavior.
    The idea is to form the conditional statements in such a way that in statements with "and" -operator
    the first operand is evaluated to False if we would run into division-by-zero situation with the second operand.
    Here we'll benefit from the fact that if Python interpreter identifies the first operand as false,
    the second operand is never evaluated.
    "Guard" is a term used for a couple of different meanings.
    The idea is that we'll be able to escape an unsafe situation as soon as possible.
    We'll return to these when discussing functions.
    
    a)
    Given the following program, 
    modify the if statement in such a way that you won't run into division by zero problems.
    Use the logical 'and' -operator to safeguard the insecure condition:
    '''
    sum_of_numbers = int(input("Sum: "))
    number_count = int(input("Number count: "))
    '''
    if (sum_of_numbers / number_count) >= 100:
      print("Average number's value is >= 100.")
    else:
      print("Average number's value is < 100.")
    '''
    if number_count > 0 and (sum_of_numbers / number_count) >= 100:
        print("Average number's value is >= 100.")

    elif number_count > 0 and (sum_of_numbers / number_count) < 100:
        print("Average number's value is < 100.")

    '''  
    b)
    Are you able to change the previous program in such a way that you can use logical 'or'-operator
    to safeguard the if statement? if so, how?
    '''

    # No idea how that would be done without making it look unnecessarily long


def task_4():
    # Task 4
    print('Task 4')
    '''
    #4 Given three numbers x, y and z. Sort the numbers without using the built-in sort() or sorted() functions.
    That is, use if statements and assignments to sort the three numbers.
    Then print them on screen in ascending order.
    At the end of the program,
    you should have variables "greatest", "middle" and "least" with the corresponding values stored in them.
    '''
    x = float(input('Give x any number: '))
    y = float(input('Give y any number: '))
    z = float(input('Give z any number: '))

    while True:
        if x > y > z:
            greatest = x
            middle = y
            least = z
            break

        else:
            if x < y:
                temp = y
                y = x
                x = temp

            if y < z:
                temp = z
                z = y
                y = temp

    print(f'Greatest: {greatest}\nMiddle: {middle}\nLeast: {least}')


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
