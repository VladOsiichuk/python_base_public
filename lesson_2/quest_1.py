def main():
    first_number_str = input("Enter first number: ")
    second_number_str = input("Enter second number: ")

    first_number = float(first_number_str)
    second_number = int(second_number_str)

    result = first_number + second_number
    print(f"Result is: {result}")


if __name__ == "__main__":
    main()
