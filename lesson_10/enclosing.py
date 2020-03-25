def add_numbers(n1):
    def add_second_number(n2):
        return n1 + n2
    return add_second_number


number_one = 3
number_two = 4

add_number3 = add_numbers(number_one)
add_number4 = add_numbers(4)
print(add_number3.__name__)
result = add_number3(number_two)
print(result)

print(add_number3(7))