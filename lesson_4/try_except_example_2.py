a = input("Enter a: ")
b = input("Enter b: ")
result = 0

try:
    number_a = int(a)
    number_b = int(b)
except ValueError as e:
    print(e)
    print("Couldn't convert inputs to numbers")
else:
    print("Successfully converted inputs to numbers")
    result = number_a / number_b
finally:
    print(f"Result is: {result}")
