def main():
    some_values = ["1", "2", "3", "4"]
    """
    map - ф-ція, що на вхід приймає ф-цію і об'єкт, по якому можна ітеруватися
    наприклад, рядок коду нижче еквівалентний ось цьому:
    number_values = list()
    for n in some_values:
       number_values.append(int(n))
    """
    number_values = list(map(int, some_values))
    print(number_values)

    some_values = ["qwer", 1, 2, [], None, 0]
    """
        filter - функція, що фільтрує об'єкт, по якому можна ітеруватися.
        на вхід приймає функцію, та ітерований об'єкт
        Якщо функція, яка передається всередину filter, повертає True, то такий об'єкт 
        додається до відфільтрованих значень
        рядок 33 еквівалентний ось цьому:
        filtered_values = list()
        for value in some_values:
            if isinstance(n, int):
                filtered_values.append(n)
        
        isinstance - функція, що перевіряє об'єкт на його тип. повертає True або False. Тобто якщо n не 
        є int, то повернеться False
        
        lambda - анонімна функція в пайтоні. Тобто функція без назви
        тобто рядок 'lambda n: isinstance(n, int)' еквівалентний наступному:
        def value_is_integer(n):
            return isinstance(n, int)  
    """
    filtered_values = list(filter(lambda n: isinstance(n, int), some_values))
    print(filtered_values)


if __name__ == "__main__":
    main()
