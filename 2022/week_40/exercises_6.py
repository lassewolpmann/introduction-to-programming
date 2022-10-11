def task_1():
    # The tuples are like lists, but immutable. However, the tuples have other advantages.
    list_ = [1, 2, 3, 'a', 'b', 'c', True, 2.5]
    tuple_ = (1, 2, 3, 'a', 'b', 'c', True, 2.5)

    # a) Import the module sys and utilise the function getsizeof().
    # Look at Python documentation to see, what it is doing.
    # Apply this function to our list and tuple. What are your observations?
    import sys

    print(f'Size of list_ in bytes: {sys.getsizeof(list_)}')
    print(f'Size of tuple_ in bytes: {sys.getsizeof(tuple_)}')

    # b) Import the module timeit. Here you use the timeit function timeit() to see the running time of the code.
    # For example, the code 2 ** 10 is run one million times.
    # timeit.timeit("2 ** 10")
    # 0.010506924998480827 seconds
    import timeit
    print(f'Calculating 2 ** 10 takes {timeit.timeit("2 ** 10")} seconds')

    # Check the running times creating the literal list like list_ and the running time of the literal like tuple_
    # How do you compare list and tuple?

    list_creation_time = timeit.timeit("list_ = [1, 2, 3, 'a', 'b', 'c', True, 2.5]")
    tuple_creation_time = timeit.timeit("tuple_ = (1, 2, 3, 'a', 'b', 'c', True, 2.5)")

    print(f'Creating the list takes {list_creation_time} seconds')
    print(f'Creating the tuple takes {tuple_creation_time} seconds')

    # c) Manipulating with tuples
    # name, age, country
    item1 = ('Charlie Brown', 11, 'USA')

    # How to derive name, age and country with unpacking of tuples?
    (name, age, country) = item1
    print(f'Name is {name}, age is {age}, country is {country}')


def task_2():
    # Here you should use list methods. Please check the table in the lecture file named Lists.

    # a) The list li contains names.
    li = ['John', 'Liza', 'Peter', 'Mary']
    # To remove the last name from li you should find a correct method.
    li.pop()
    print(li)

    # b) Add the name ‘Charlie’ between ‘Liza’ and ‘Peter’ using an appropriate method.
    li.insert(li.index('Peter'), 'Charlie')
    print(li)

    # c) String has a method join(). Explain, how to use it.
    # Then apply join to print all the names of li with each name on its own line.
    print('\n'.join(li))

    # d) Make a program that asks a small number n. The program prints stars with n columns and n rows.
    # Expected output: Give me a small number: 4
    # ****
    # ****
    # ****
    # ****
    # Hint: Apply the multiplication operator * to string and lists. join() may be useful too.
    small_number = int(input('Give a small number (1-10): '))
    print(small_number * f'{small_number * "*"}\n')


def task_3():
    # This exercise uses functions of random module and ranges and lists.
    # list(range(1, 4)) returns [1, 2, 3]

    # a) Your program prints [2, 4, 6, 8, 9, 7, 5, 3, 1] using range and + operator.
    print(list(range(2, 9, 2)) + list(range(9, 0, -2)))

    # b) The code
    import random
    li = ['John', 'Liza', 'Peter', 'Mary']
    # should give a random word
    print(random.choice(li))

    # c) We roll a die 12 times
    rolls = random.choices(range(1, 7), k=12)
    print(rolls)

    # How many 6’s are there?
    print(f"The list contains {rolls.count(6)} 6's")

    # d) The Finnish lottery takes 7 random integers between 1-40 (both included).
    fin_lot = random.sample(range(1, 41), 7)

    # Sort the numbers from the smallest to the greatest.
    fin_lot.sort()
    print(fin_lot)


def task_4():
    # We have a deck of playing cards.
    suits = ['♣', '♦', '♥', '♠']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(s, v) for s in suits for v in values]

    # a)
    # Calculate the number of the cards of the deck.
    card_count = len(deck)

    # b) Change the suit of the second card ('♣', '3') to the card (‘♠’, '3').
    # What are your notions and why?
    deck[1] = (suits[3], values[1])
    print(deck)

    # c) Shuffle the deck
    # Take one random card and print it in the form e.g. ♣K
    import random

    random_card = random.choice(deck)
    print(f'{random_card[0]}{random_card[1]}')

    # d) Deal the cards for 4 players.
    cards_per_player = card_count // 4
    for player in range(4):
        player_cards = []
        for c in range(cards_per_player):
            r_card = random.choice(deck)
            deck.pop(deck.index(r_card))
            player_cards.append(r_card)

        print(f'Cards for Player {player + 1} are {player_cards}')


if __name__ == '__main__':
    task_1()
    task_2()
    task_3()
    task_4()
