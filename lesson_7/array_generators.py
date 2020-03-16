def get_only_digits_array(arr):
    """
    :param arr: list of some values
    :return: list of values which are digits
    """

    """
    Дана функція еквівалентна наступним рядкам
    output_array = list()
    for n in arr:
        if isinstance(n, int) or n.isalpha():
            output_array.append(n)
    """
    return [
        n for n in arr
        if isinstance(n, int) or
        (isinstance(n, str) and n.isalpha())
    ]


def get_values_from_nested_arrays_to_one_array(arr):
    """
    :param arr: Array of nested arrays (matrix)
    :return: Array with values from nested arrays
    """

    """
    Ця функція еквівалентна наступним рядкам
    output_value = list()
    for i in arr:
        if not isinstance(i, list):
            i = [i]
        for value in i:
            output_array.append(value)
    return output_value
    """
    return [
        value for i in arr for value in
        ([i] if not isinstance(i, list) else i)
    ]


def main():

    """
    Генерація списку зі значень від 0 до 9
    """

    """
    Рядок нижче еквівалентний ось цьому
    arr = list()
    for i in range(10):
        arr.append(i)
    """
    arr = [i for i in range(10)]
    print(arr)
    print(type(arr))


if __name__ == "__main__":
    main()
