def search_value_index_in_nested_array(array, value, include_parent_index=True):
    for i in range(len(array)):
        if isinstance(array[i], list):
            for j in range(len(array[i])):
                if value == array[i][j]:
                    if include_parent_index:
                        return i, j
                    return j


def main():
    arr = [1, 2, [3, 5, 1]]
    print(search_value_index_in_nested_array(arr, 3))


if __name__ == "__main__":
    main()
