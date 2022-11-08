def task_1():
    import random

    def single_die_roll() -> int:
        return random.randint(1, 6)

    def n_die_rolls(n: int):
        print(random.choices(range(1, 7), k=n))

    def return_n_die_rolls(n: int) -> list:
        return random.choices(range(1, 7), k=n)

    # Roll a die and return the result.
    roll_value = single_die_roll()

    # Roll a die n times and print the results.
    n_die_rolls(6)

    # Roll a die and return the results as a list.
    roll_list = return_n_die_rolls(10)


def task_2():
    def string_to_tuple(s: str) -> tuple:
        s_tuple = (s[0], s[-1])

        return s_tuple

    def dot_product_of_vectors(v1: list, v2: list) -> int:
        dot_product = 0
        if len(v1) == len(v2):
            for n in range(len(v1)):
                dot_product += v1[n] * v2[n]

        else:
            pass

        return dot_product

    # The function takes a string and returns the first and the last letter as a tuple.
    string = 'This is a string'
    first_last_tuple = string_to_tuple(string)

    # The dot product of two vectors. A vector is like vec1 = [3, 2, 5] and vec2 = [1, 3, 2]
    # The dot product is defined like 3*1 + 2*3 + 5*2 = 19 and is returned.
    vec1 = [3, 2, 5]
    vec2 = [1, 3, 2]
    dot_product_result = dot_product_of_vectors(vec1, vec2)


def task_3():
    def get_sentence() -> tuple:
        """
        Give the subject, verb and object.

        If the desired sentence in normal language is "This is my home.", the subject would be "This", the verb would
        be "is", and the object would be "my home"

        :return: Tuple containing the subject, verb, and object.
        """

        sentence_list = (input('Subject: '), input('Verb: '), input('Object: '))

        return sentence_list

    def create_yoda_sentence(sentence: tuple):
        """
        Given the sentence in form of a tuple, the function rearranges the values into a Yoda-type sentence and
        prints it out.
        """

        s: str
        v: str
        o: str

        (s, v, o) = sentence

        if s == 'I' or s == 'i':
            s = s.capitalize()

        else:
            s = s.lower()

        yoda_sentence = f'{o.capitalize()}, {s} {v}.'

        print(yoda_sentence)

    normal_sentence = get_sentence()
    create_yoda_sentence(normal_sentence)


def task_4():
    import random

    def bound_ratio_calculation(b: float, r: float):
        for i, f in enumerate(float_list):
            # If a value in the list exceeds the bound
            if f > b:
                # the value in the list is replaced by the original value multiplied with the ratio
                float_list[i] *= r

    float_list = [random.uniform(0, 1) for _ in range(10)]  # a list of 10 floats (all values between [0, 1))
    bound_value = random.uniform(0, 1)                      # 0 ≤ bound < 1 as a float
    ratio_value = random.uniform(0, 1)                      # 0 ≤ ratio < 1 as a float

    bound_ratio_calculation(bound_value, ratio_value)


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
