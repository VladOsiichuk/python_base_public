"""
quadratic equation
"""


def get_discriminant(b, a, c):
    """
    equation = ax^2 +- bx +- c
    :param b: middle value in equation
    :param a: first value in equation
    :param c: last value in equation
    :return: discriminant
    """

    d = b ** 2 - 4 * a * c
    return d


def get_one_decision(b, a):
    """
    :param b: param from equation
    :param a: param from equation
    :return: one decision for  equation
    """

    x = -(b / (2 * a))
    return x


def get_two_decisions(b, d, a):
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    return x1, x2


def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    d = get_discriminant(b, a, c)
    if d < 0:
        print("Equation has no decisions")
        return

    # equation has more than one decision
    elif d > 0:
        result = get_two_decisions(b, d, a)

    # just one decision exists
    else:
        result = get_one_decision(b, a)

    print(f"Result is: {result}")


if __name__ == "__main__":
    main()
