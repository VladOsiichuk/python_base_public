def main():
    """Context manager example"""

    """
    Оператор with означає початок конструкції контекстного менеджера
    Відкритий файл буде присвоєно змінній f
    Даний контекстний менеджер закриє файл автоматично
    Тобто вкінці вже не треба писати f.close()
    Код нижче еквівалентний наступному кодові
    f = open("students.txt", "r")
    print(f.read())
    f.close()
    """
    with open("students.txt", "r") as f:
        data = f.read()
        pass
        # print(f.read())


if __name__ == "__main__":
    main()
