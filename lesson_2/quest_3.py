"""
Написати програму для обчислення площі трикутника за трьома сторонами;
Результат вивести на екран.
"""


def main():
    """
    s = (p * (p-a) * (p-b) * (p - c)) ** 0.5
    """

    a = float(input("Введи першу сторону: "))
    b = float(input("Введи другу сторону: "))
    c = float(input("Введи третю сторону: "))

    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

    print(f"Результат: {s}")


if __name__ == "__main__":
    main()