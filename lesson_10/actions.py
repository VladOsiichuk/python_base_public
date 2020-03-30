
import json
from helpers import file_exists
# TODO:  
"""
Створити декоратор, який перевірятиме, чи існує файл у файловій системі.
тобто до add_article додати декоратор @file_exists("articles.json"), 
Який перевіритть, чи існує файл. Якщо такого файлу нема, то створити його
"""

def show_list_of_articles():
    pass

# @file_exists("articles.json")
def add_article():
    """
    Отримати від користувача назву статті та тіло статті
    """

    title = input("Enter title: ")
    body = input("Enter body: ")

    with open("articles.json", "r") as f:
        data_dict = json.loads(f.read())
    
    data_dict[title] = body

    with open("articles.json", "w") as f:
        data_to_write = json.dumps(data_dict)
        f.write(data_to_write)


def remove_article():
    pass
