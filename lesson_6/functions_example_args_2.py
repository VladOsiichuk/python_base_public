def add_strings(*args, delimiter=" "):
    result = ""
    for s in args:
        result += s + delimiter
    return result


def main():
    whole_string = add_strings("test", "other", "one_more")
    print(whole_string)


if __name__ == "__main__":
    main()
