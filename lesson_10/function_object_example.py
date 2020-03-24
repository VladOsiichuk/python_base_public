ADMIN_CREDENTIALS = {
    "username": "admin",
    "password": "1234567"
}
EDITOR_CREDENTIALS = {
    "username": "Editor",
    "password": "123"
}
VISITOR_CREDENTIALS = {
    "username": "Visitor",
    "password": "11"
}


def show_list_of_articles():
    pass

def add_article():
    pass

def remove_article():
    pass

def get_admin_actions():

    print("You can do the following actions: ")
    print("1. See the list of articles. (Enter 1)")
    print("2. Add new articles. (Enter 2)")
    print("3. Remove articles (Enter 3)")
    return [1, 2, 3]    


def get_editor_actions():
    print("You can do the following actions: ")
    print("1. See the list of articles. (Enter 1)")
    print("2. Add new articles. (Enter 2)")
    return [1, 2]


def get_visitor_actions():
    
    print("You can do the following actions: ")
    print("1. See the list of articles. (Enter 1)")
    return [1]


def get_input(prompt, required=True):
    while True:
        value = input(f"{prompt}: ")
        if not value and required:
            print("Please try again. ")

        else:
            return value


def show_user_menu(role_actions_func):
    actions = role_actions_func()

    handlers = {
        1: show_list_of_articles,
        2: add_article,
        3: remove_article
    }

    while True:
        action = input("Enter your action: ")
        if int(action) not in actions:
            print("This is a bad action. Try again")
        
        handler = handlers[action]
        return handler()

def login():
    while True:
        username, password = input("Please enter your username and password "), input("Please enter your username and password")
        if not username and not password:
            print("Credentials are incorrect. Try again")

        else:
            user_role = ""
            if username == ADMIN_CREDENTIALS["username"] and password == ADMIN_CREDENTIALS["password"]:
                user_role = "ADMIN"
            if username == EDITOR_CREDENTIALS["username"] and password == EDITOR_CREDENTIALS["password"]:
                user_role = "EDITOR"
            if username == VISITOR_CREDENTIALS["username"] and password == VISITOR_CREDENTIALS["password"]:
                user_role = "VISITOR"
            
            if user_role:
                return user_role


def main():
    role = login()

    menu_actions = {
        "ADMIN": get_admin_actions,
        "EDITOR": get_visitor_actions,
        "VISITOR": get_visitor_actions
    }
    menu = menu_actions[role]
    show_user_menu(menu)


if __name__ == "__main__":
    main()