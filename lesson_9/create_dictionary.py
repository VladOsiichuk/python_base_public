def main():
    """
    Ключі в словнику мають бути незмінним типом даних
    Тобто ключем можуть виступати рядки, числа, кортежі
    """

    value = "12345"
    arr = [1, 2, 3]
    d1 = {"Key": "some_value", 1: "other_value", "4": value, "array": arr}

    d2 = dict(array=arr, value=value, Key="some_value")
    names_and_ages = [["Vlad", 18], ["Sasha", 21], ["Serhiy", 15]]
    d3 = {row[0]: row[1] for row in names_and_ages}


if __name__ == "__main__":
    main()
