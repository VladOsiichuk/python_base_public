from lesson_11.inheritance_1 import Square

s = Square()

class A:
    
    def __init__(self, arg_1):
        self.value = arg_1

    def print(self):
        print("Method from class A called")
        print(self.value)

class B(A):
    """
    В даному випадку клас В наслідуєтсья від класу А
    Це означає, що клас В матиме всі поля і методи класу А
    """

    def __init__(self, arg_1):
        """
        Якщо ми наслідуємося від якогось класу, то в даному методі повинні викликати 
        super().__init__, щоб ініціалізувати базовий клас, тобто клас А
        """
        self.data = {}
        super().__init__(arg_1)
        

    def print_other(self):
        print("Method from class B called")

b = B(1)
b.print()
data = {"data": 1}
b.print_other()

