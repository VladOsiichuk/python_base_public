"""
Вводиться два числа. Знайти найбільший спільний дільник цих чисел;
"""

first = int(input("Enter first n: "))
second = int(input("Enter second n: "))

"""
if first < second: 
    to = first
else:
    to = second
"""
to = first if first < second else second
max_div = 0
for i in range(1, to + 1):
    if first % i == 0 and second % i == 0:
        max_div = i
print(max_div)