"""
Програма, яка конвертує десяткове значення
у двійкове
"""


# # отримати дані від користувача
number = int(input("Enter a number: "))

# створити змінну, яка міститиме в собі послідовність нулів і одиниць
result = ""

# повторювати дії у вкладеному блоці з кодом, доки number буде більшим від нуля
while number > 0:
    result += str(number % 2)  # додати до нашої змінної остачу від ділення на 2
    number //= 2  # поділити число на 2, без остачі

# перевернути наш рядок
result = result[::-1]

# вивести результат на екран
print(result)
