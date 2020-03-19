def main():
    file = open("sample.txt", "r")
    lines = file.readlines()

    position = int(input("Position: "))
    line = input("Line: ") + "\n"

    lines.insert(position - 1, line)
    file.close()
    file = open("sample.txt", "w")

    file.writelines(lines)
    file.close()


if __name__ == "__main__":
    path = input("Please enter file path: ")
    file = open(path, "r+")
    string = input("Enter string to paste into file: ")
    place = int(input("Enter line number in file to place string: "))
    lines_before = open(path, "r+").readlines()[:place]
    lines_after = open(path, "r+").readlines()[place - 1:]
    new_file = "".join(lines_before) + string + "\n" + "".join(lines_after)
    file.write(new_file)
    file.close()


