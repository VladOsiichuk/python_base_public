number = int(input("Enter a number: "))
result = ""

while number > 0:
    result += str(number % 2)
    number //= 2

result = result[::-1]
print(result)
