def main():

    file = open("test.txt", "w+")
    print(file.read(5))
    file.write("qwe")
    file.close()


if __name__ == "__main__":
    main()
