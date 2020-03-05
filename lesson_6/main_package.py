from lesson_6.package_example.helpers import list_generators


def main():
    print(list_generators.get_list_of_random_nums(10))
    print(list_generators.get_list_of_random_chars(3))

    print(__name__)


if __name__ == "__main__":
    main()
