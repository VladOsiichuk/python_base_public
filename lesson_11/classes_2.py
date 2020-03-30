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


me = Human(19, "Vlad", "M")
me.change_name("Vladyslav")
print(me.name)