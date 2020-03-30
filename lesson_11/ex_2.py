"""Створити базовий клас File.Створити два інші класи (JsonFile, TxtFile),
які наслідуватимуться від нього. Для даних класів реалізувати методи open_file, write_to_file.
для JsonFile інформація у файл повинна записуватися у форматі json. Які атрибути повинні бути у класів:
filename. Реалізувати також метод get_file_extension, який повертатиме формат файлу."""
import json


class File:
    def __init__(self, file_path, file_name):
        self.path = file_path
        self.file_name = file_name
        self.full_path = self.path + "/" + self.file_name
        self.file_ext = self.file_name.split(".")[1]

    def get_file_extension(self):
        return self.file_ext
    
    def __str__(self):
        return self.file_name


class JsonFile(File):

    def __init__(self, file_path, file_name):
        super().__init__(file_path, file_name)


    def open_file(self):
        with open(self.full_path, "r") as file:
            data = json.load(file)
            return data

    def write_file(self, data):
        with open(self.full_path, "w") as file:
            data = json.dumps(data)
            file.write(data)


class SomeClass:
    def __init__(self, field_1, field_2):
        self.field_1 = field_1
        self.field_2 = field_2


class TxtFile(File):
    def __init__(self, file_path, file_name):

        super().__init__(file_path, file_name)
        print(self.full_path)

    def open_file(self):
        with open(self.full_path, "r") as file:
            data = file.read()
            return data

    def write_file(self, data):
        with open(self.full_path, "w") as file:
            file.write(data)

    def copy_data_from_other_class(self, other_object):
        self.field_from_txt_1 = other_object.field_1
        self.field_from_txt_2 = other_object.field_2

# json_file = JsonFile(".", "test.json")

txt_file = TxtFile(".", "test.txt")
obj = SomeClass("field data 1", "field data 2")
txt_file.copy_data_from_other_class(obj)

print(txt_file.field_from_txt_2)

# txt_file.write_file("123")
# txt_file.get_file_extension()
# print(txt_file.full_path)

# print(txt_file.file_ext)

# json_file.write_file({"data": "1"})
# print(json_file.open_file())

# json_file.get_file_extension()
# print(json_file.file_ext)