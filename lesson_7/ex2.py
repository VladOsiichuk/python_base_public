def str_to_int(s):
    result = ""
    for c in s:
        if c.isdigit():
            result += c
    return int(result)


print(str_to_int("ewr123") == str_to_int("1sd23"))


def str_to_int_v2(s):
    # ewr123
    return int(
        "".join(
            list(filter(lambda c: c.isdigit(), s)
            )
        )
    )


print(str_to_int_v2("ewr123") == str_to_int_v2("1sd23"))

