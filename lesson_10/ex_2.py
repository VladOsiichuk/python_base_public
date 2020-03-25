n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))

action = input("What should we do with numbers? Enter '*', '+', '-', '/': ")

def add_numbers(n1, n2):
    return n1 + n2

def multiply_numbers(n1, n2):
    return n1 * n2

def minus_numbers(n1, n2):
    return n1 - n2

def divide_numbers(n1, n2):
    return n1 / n2


def run_execution(func, n1, n2):
    """
    """
    result = func(n1, n2)
    print(result)

# if action == "*":
#     func = multiply_numbers
# elif action == "/":
#     func = divide_numbers
# elif action == "-":
#     func = minus_numbers
# elif action == "+":
#     func = add_numbers

functions = {
    "*": multiply_numbers,
    "+": add_numbers,
    "/": divide_numbers,
    "-": minus_numbers
}
func = functions[action]
run_execution(func, n1, n2)
