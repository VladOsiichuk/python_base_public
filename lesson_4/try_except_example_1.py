a = input("Enter a: ")
b = input("Enter b: ")
number_a, number_b = None, None
result = 0
try:
    number_a = int(a)
    number_b = int(b)
except ValueError:
    print("Couldn't convert inputs to numbers")

if number_a is not None and number_b is not None:
    result = number_a / number_b

print(f"Result is: {result}")
