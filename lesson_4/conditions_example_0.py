from termcolor import colored

username = input("Enter your name: ")
user_color = input("Enter color name (R, G, B): ")

if user_color == "R":
    text = colored(f"Your name is {username}", "red")
    print(text)
elif user_color == "G":
    text = colored(f"Your name is {username}", "green")
    print(text)
elif user_color == "B":
    text = colored(f"Your name is {username}", "blue")
    print(text)
else:
    print("\nError. Entered color is invalid\n")
