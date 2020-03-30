class FileManager:

    def __init__(self):
        self.data_file = None
        self.__password = None

    def open_file(self, filepath):
        with open(filepath, "r") as f:
            self.data_file = f.read()
        
        return self._decode_file()

    def __get_password(self):
        """
        Коли метод починається на дві нижні риски, то це означає, що це приватний метод класу.
        Його не можна буде викликати у основній програмі. Він доступний тільки в межах класу.
        """
        self.__password = input("Enter password: ")

    def _decode_file(self):
        """
        Коли метод починається на одну нижню риску, то це означає, що це захищений (protected) метод
        Викликати такі методи прийнято тільки всередині класу та пакетів, 
        хоч їх і можна викликати із головної програми.
        """
        if getattr(self, "__password", None) is None:
            self.__get_password()
        print("decoding... ")

m = FileManager()

# m.open_file("test.txt")
# print(m.data_file)
print(m._decode_file())

print(m.__get_password())