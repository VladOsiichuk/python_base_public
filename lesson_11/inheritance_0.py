class A:
    
    def __init__(self, value):
        self.value = value

    def print(self):
        print("Method from class A called")
        print(self.value)

class B(A):
    """
    В даному випадку клас В наслідуєтсья від класу А
    Це означає, що клас В матиме всі поля і методи класу А
    """

    def __init__(self, value):
        """
        Якщо ми наслідуємося від якогось класу, то в даному методі повинні викликати 
        super().__init__, щоб ініціалізувати базовий клас, тобто клас А
        """

        super().__init__(value)

    def print_other(self):
        print("Method from class B called")
        print(self.value)

b = B(1)
b.print()