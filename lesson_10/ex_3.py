n = int(input("Введіть число, на яке будуть ділитися інші значення: "))

def divide_on(n):
    def divide_number(n2):
        return n2 / n
    return divide_number

division_function = divide_on(n)

while True:
    other_number = int(input("Введіть число, яке хочете поділити: "))
    result = division_function(other_number)
    print(f"Result: {result}")