import random
from .simple_generators import get_random_char


def get_list_of_random_nums(array_length, max_value=100, min_value=0):
    arr = list()
    for i in range(array_length):
        random_value = random.randint(min_value, max_value)
        arr.append(random_value)
    return arr


def get_list_of_random_chars(array_length):
    arr = list()
    for i in range(array_length):
        char = get_random_char()
        arr.append(char)
    return arr
