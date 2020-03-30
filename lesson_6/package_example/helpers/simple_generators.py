import random
from string import ascii_letters


def get_random_char():
    return random.choice(ascii_letters)


def get_random_name():
    names = ["Vlad", "Vadym", "Stepan", "Iryna", "Kateryna"]
    return random.choice(names)
