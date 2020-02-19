def main():
    first_number = float(input("First number: "))
    second_number = float(input("Second number: "))
    third_number = float(input("Third number: "))

    sum_ = sum([first_number, second_number])
    is_greater = sum_ >= third_number

    print(is_greater)


if __name__ == "__main__":
    main()
