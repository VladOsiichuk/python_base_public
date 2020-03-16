import re


def main():

    # Витягти із рядка всі слова англійською мовою
    text = "Some text. Текстова інформація. Gg"
    result = re.findall("[a-zA-Z]+", text)
    print(result)

    # Перевірити, чи даний рядок підходить певному шаблону
    text = "123456"
    result = re.match("123456", text)
    print(bool(result))

    # Перевірка, чи є у введеному рядку числа
    text = "123456"
    result = re.match("[0-9]+", text)
    print(bool(result))

    # Перевірка, чи введено у рядку тільки числа
    text = "123456A"
    result = re.fullmatch("[0-9]+", text)
    print(bool(result))


if __name__ == "__main__":
    main()
