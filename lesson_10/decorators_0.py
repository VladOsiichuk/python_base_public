def simple_decorator(f):
    """
    f - це наша функція, яку ми огорнули даним декоратором
    """

    def wrapped():
        print("Виконання коду ПЕРЕД функцією")
        f()
        print("Виконання коду ПІСЛЯ функції")

    return wrapped


@simple_decorator
def some_function():
    print("Виконання коду всередині функції")


def main():
    """
    функція some_function огорнута декоратором simple_decorator
    це означає, що перед виконанням самої функції, 
    код виконається спочатку всередині самого декоратора. 
    """

    some_function()

if __name__ == "__main__":
    main()