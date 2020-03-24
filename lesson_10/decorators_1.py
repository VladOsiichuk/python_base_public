import os


def file_exists(f):
    def wrapper(file_path):
        """
        file_path - це аргумент, який приймає функція, що була огорнута 
        даним декоратором
        Тобто це аргумент, що був переданий у рядку 27 у функції main
        """
        if os.path.exists(file_path):
            return f(file_path)
        else:
            print(f"File with specified path {file_path} does not exists")
    return wrapper


@file_exists
def get_data_from_file(file_path):
    file = open(file_path, "r")
    lines = file.readlines()
    file.close()
    return lines


def main():
    data = get_data_from_file("file.txt")


if __name__ == "__main__":
    main()
