class Human:
    def __init__(self, age, name, sex):
        print(f"Start init new object with values: {age} {name} {sex}")
        self.age = age
        self.name = name
        self.sex = sex

    def change_name(self, new_name):
        """
        Ми можемо міняти поля об'єкта знову ж таки через 'self'
        """
        self.name = new_name

    def __str__(self):
        return f"{self.name}, {self.age}, {self.sex}"



me = Human(19, "Vlad", "M")
print(me)
# me.change_name("Vladyslav")
# me.some_field = 1
# print(me.some_field)
# print(me.name)

