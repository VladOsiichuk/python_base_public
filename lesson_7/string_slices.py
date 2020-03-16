def main():
    s = "abcdefghijklmn"

    # Отримати перших 5 літер зі строки
    first_five_letters = s[:5]
    print(f"first five letters: {first_five_letters}")

    second_and_third_values = s[1:3]
    print(f"Second and third values: {second_and_third_values}")

    """
    Отримати останніх 5 літер. Від'ємний індекс означає
    рахувати з кінця рядка. Тобто новій змінній буде присвоєно значення
    від -5 символу (а це 'j') включно і до кінця рядка
    s = "abcdedfghijklmn"
    """
    last_five_letters = s[-5:]
    print(f"Last five letters: {last_five_letters}")

    # Отримати непарні символи в рядку
    odd_chars = s[1::2]
    print(f"Odd chars: {odd_chars}")

    # Перевернути рядок
    # s = "abcdedfghijklmn"
    reversed_string = s[::-1]
    print(f"Reversed string: {reversed_string}")


if __name__ == "__main__":
    main()
