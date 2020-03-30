# Run this program 'python random_choice.py 1 2 3 4 5 6'

import random


def main(args):
    print(args)
    print(random.choice(args))


if __name__ == "__main__":
    import sys
    main(sys.argv)
