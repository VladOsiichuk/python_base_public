import time
ADMIN_PASSWORD = "12345"
EDITOR_PASSWORD = "123456"
STAFF_PASSWORD = "1234567"

password_to_role_mapping = {
    ADMIN_PASSWORD: "ADMIN",
    EDITOR_PASSWORD: "EDITOR",
    STAFF_PASSWORD: "STAFF"
}


def user_has_access(allowed_role):
    def wrapper(f):
        def wrapped(password):
            print("ALLOWED ROLE", allowed_role)
            print("password", password)
            actual_role = password_to_role_mapping.get(password)
            print("ACTUAL ROLE", actual_role)
            print("FUNCTION", f.__name__)
            if actual_role is None or actual_role != allowed_role:
                print("You don't have permission to perform this action")
            else:
                return f()
        return wrapped
    return wrapper


@user_has_access("ADMIN")
def create_article(*args, **kwargs):
    print("Here we create some article")
    title=get_input("Enter a title to article"), 
    content=get_input("Enter content", required=False)
    return {"title": title, "content": content}


def login():
    while True:
        password = input("Enter password: ")
        if not password:
            print("Try again")
            time.sleep(1)
        else:
            return password

def get_input(prompt, required=True):
    while True:
        value = input(f"{prompt}: ")
        if not value and required:
            print("Please try again. ")

        else:
            return value


def main():
    password = login()
    create_article(password=password)


if __name__ == "__main__":
    main()