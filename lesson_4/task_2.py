"""
Вводиться число. Написати програму, яка перевіряє, чи дане число є паліндромом.
Тобто, якщо перевернути таке число, то його значення не зміниться.
Наприклад, число 636 є паліндромом, 123 - ні.
Число може мати значення від 1 до 999
"""

number = int(input("Enter number: "))

if 1 < number < 100:
    right_digit = number // 10
    left_digit = number % 10

    if left_digit == right_digit:
        print("Число є паліндромом")
    else:
        print("Число не є паліндромом")

elif 100 <= number < 1000:
    right_digit = number // 10
    left_digit = number % 100

    if left_digit == right_digit:
        print("Число є паліндромом")
    else:
        print("Число не є паліндромом")
