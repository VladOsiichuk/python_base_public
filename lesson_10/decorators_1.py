import os


def file_exists(f):
    def wrapper(file_path):
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
    pass


if __name__ == "__main__":
    main()
