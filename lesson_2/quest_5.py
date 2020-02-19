def main():
    first_number = float(input("Enter first number: "))

    print("Квадрат числа:", first_number ** 2)
    print("Корінь числа:", first_number ** 0.5)

    second_number = float(input("Enter second number: "))

    print("Остача від ділення:", first_number % second_number)
    print("Частка:", first_number / second_number)


if __name__ == "__main__":
    main()
