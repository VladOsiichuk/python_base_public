"""
Користувач вводить два числа від 1 до 6.
Якщо сума чисел парна і перше число більше за друге, то вивести на екран,
що користувач виграв машину. Якщо друге число більше, ніж перше - квартиру. Якщо число непарне,
то вивести на екран, що користувач нічого не виграв. Якщо конвертувати введені дані в чисельний
тип не вдалося, повідомити користувачеві, що він ввів неправильні дані
"""

try:
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))

    if not 1 <= number_1 <= 6 or not 1 <= number_2 <= 6:
        raise ValueError("Your input is incorrect")
except ValueError as e:
    print(e)
    exit()

if (number_1 + number_2) % 2 == 0:
    if number_1 > number_2:
        print("You won a car")
    else:
        print("You won a flat")
else:
    print("You are looser! :)")
