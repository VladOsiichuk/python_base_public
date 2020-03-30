from readlines import func_other


def main():
    func_other()
    file = open("sample.txt", "r")
    while True:
        first_line = file.readline()
        print(first_line, end="")

        if not first_line:
            break


if __name__ == "__main__":
    main()
