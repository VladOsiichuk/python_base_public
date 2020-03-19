def main():
    file = open("students.txt", "r")
    data = file.readlines()
    print(data)


def func_other():
    print("Func other called")


if __name__ == "__main__":
    main()
    func_other()
