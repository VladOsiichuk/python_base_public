"""Створити три класи. Кожен з них повинен мати один атрибут: value.
Для першого класу value буде типу str, для другого - list, для третього - dict.
Для кожного класу реалізувати метод sort(). Цей метод повинен відсортувати атрибут класу value,
не змінивши його типу. Для словника сортування має бути за ключем. Ключі при сортуванні конвертувати у тип str"""


class StrSort:
    def __init__(self, value):
        self.value = value
        self.sorted_value = None

    def sort(self):
        self.sorted_value = sorted(self.value)
        return "".join(self.sorted_value)


class ListSort:
    def __init__(self, value):
        self.value = value
        self.sorted_value = None

    def sort(self):
        # self.sorted_value = self.value.sort()
        return sorted(self.value)

class DictSort:
    def __init__(self, value):
        self.value = value
        self.sorted_value = None

    def sort(self):
        keys = list(self.value.keys())
        str_keys = list(map(str, keys))
        data = {}
        # for key, value in self.value.items():
        #     data[str(key)] = value

        for key in sorted(str_keys):
            if key.isdigit():
                key = int(key)
            data[key] = self.value[key]
        self.sorted_value = data
        return self.sorted_value


sort_string = StrSort("badc6097").sort()

sort_list = ListSort([1, 2, 4, 5, 6, 3]).sort()

sort_dict = DictSort({3:1, 2:5, "f": 4, "a": 3}).sort()

print(sort_string)
print(sort_list)
print(sort_dict)