"""
Користувач вводить строку і пошукове слово.
Вивести на екран, скільки разів пошукове слово зустрічається в строці.
Регістр не враховувати

"""
import re

def search(s, search_word):
    return len(re.findall(f"[{search_word}]", s))

print(search("a asd sdd a, a ", "a"))