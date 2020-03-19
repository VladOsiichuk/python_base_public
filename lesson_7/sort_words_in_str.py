"""
Користувач вводить речення.
Відсортувати слова в даному реченні
у алфавітному порядку і результат вивести на екран.
"""

def sort_sentence(s):
    arr = s.split()
    arr.sort()

    return " ".join(arr)

print(sort_sentence("Good. London is the capital of Great Britain"))

