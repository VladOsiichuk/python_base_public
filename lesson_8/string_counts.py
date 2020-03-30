def main():
    with open("sample_copy.txt", "a+") as f:
        f.seek(0)
        counter = 0
        while True:
            row = f.readline()
            print(row, end="")

            if not row:
                break

            f.seek(counter)
            row = "".join([f"{word}{len(word)} " for word in row.split()])
            row += "\n"
            f.write(row)
            counter += len(row)




    return
    with open("sample_2.txt", "w") as f:
        for line in lines:
            string_with_counts = ""
            for word in line.split():
                string_with_counts += f"{word}{len(word)} "
            string_with_counts += "\n"
            f.write(string_with_counts)

    with open("sample_2.txt", "w") as f:
        new_line = ""
        for line in lines:
            arr = [f"{word}{len(word)} " for word in line.split()]
            new_line += "".join(arr)
            new_line += "\n"
        f.write(new_line)


if __name__ == "__main__":
    main()
