
s = input("Enter number")
if s.isdigit():
    print("entered value is number")
else:
    print("entered value is  NOT a number")


def get_int():
    while True:
        value = input("Enter a number: ")
        if value.isdigit():
            return int(value)
        else:
            print("Entered value is incorrect. Try again. ")
get_int()