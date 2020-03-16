def get_only_digits_array(arr):
    """
    :param arr: list of some values
    :return: list of values which are digits
    """
    print(arr)
    """
    Дана функція еквівалентна наступним рядкам
    output_array = list()
    for n in arr:
        if isinstance(n, int) or (isinstance(n, str) and n.isdigit()):
            output_array.append(n)
    return output_array
    """
    output_array = [
        n for n in arr
        if isinstance(n, int) or
        (isinstance(n, str) and n.isdigit())
    ]
    return output_array


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
    """
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9], 
     10]
    """

    output_value = [
        value for nested_array in arr for value in
        ([nested_array] if not isinstance(nested_array, list) else nested_array)
    ]

    return output_value


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
    # arr = [i for i in "Python"]
    # print(arr)
    # print(type(arr))


    # print(get_only_digits_array(["1", 2, "3", "a", "b"]))
    print(get_values_from_nested_arrays_to_one_array([[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     10]))

if __name__ == "__main__":
    main()
