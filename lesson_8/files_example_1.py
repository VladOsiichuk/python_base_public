def get_file_to_read(path):
    """
    Якщо в операційній системі файлу зі вказаним шляхом не існує,
    і ви хочете відкрити його на читання,
    то в такому випадку з'явиться помилка
    :param path: path to file
    :return: file object or None
    """

    file = None
    try:
        file = open(path, "r")
    except FileNotFoundError:
        print(f"File {path} not found")
    return file


def main():

    file = get_file_to_read("students.txt")
    if file is None:
        return

    data_from_file = file.read()
    print(data_from_file)
    file.close()

if __name__ == "__main__":
    main()
