def task_1():
    # Roll a die and return the result.
    roll_value = single_die_roll()

    # Roll a die n times and print the results.
    n = 6
    n_die_rolls(n)

    # Roll a die and return the results as a list.
    n = 10
    roll_list = return_n_die_rolls(n)


def single_die_roll():
    import random

    return random.randint(1, 6)


def n_die_rolls(n):
    import random
    print(random.choices(range(1, 7), k=n))


def return_n_die_rolls(n):
    import random

    return random.choices(range(1, 7), k=n)


def task_2():
    # The function takes a string and returns the first and the last letter as a tuple.
    s = 'This is a string'
    s_tuple = string_to_tuple(s)

    # The dot product of two vectors. A vector is like vec1 = [3, 2, 5] and vec2 = [1, 3, 2]
    # The dot product is defined like 3*1 + 2*3 + 5*2 = 19 and is returned.
    vec1 = [3, 2, 5]
    vec2 = [1, 3, 2]
    dot_product = dot_product_of_vectors(vec1, vec2)


def string_to_tuple(s):
    s_tuple = (s[0], s[-1])
    return s_tuple


def dot_product_of_vectors(v1, v2):
    dot_product = 0
    if len(v1) == len(v2):
        for n in range(len(v1)):
            dot_product += v1[n] * v2[n]

    else:
        pass

    return dot_product


def task_3():
    pass


def task_4():
    import random
    # Write a method that gets as an argument ︎a list of floats (all values between [0, 1)),
    # ︎0 ≤ bound < 1 as a float, and
    # 0 ≤ ratio < 1 as a float and then examines all values in the list one by one.
    # If a value in the list exceeds the bound then the value in the list is replaced by the original value
    # multiplied with the ratio.
    # The method must modify the original list that was given, and it must not print or return anything.
    global float_list
    float_list = []
    for i in range(random.randint(5, 20)):
        float_list.append(random.uniform(0, 1))

    bound = random.uniform(0, 1)
    ratio = random.uniform(0, 1)

    bound_ratio_calculation(bound, ratio)


def bound_ratio_calculation(bound, ratio):
    for index, f_value in enumerate(float_list):
        if f_value > bound:
            float_list[index] *= ratio

        else:
            pass


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
