s = "Vlad"
step = 1
from string import ascii_lowercase
"""
zak
1
"""
# abcdefghijklmnopqrstuvwxyz


def encrypt(s, step):
    result = ""
    for c in s:
        new_index = ascii_lowercase.index(c) + step
        if new_index >= len(ascii_lowercase):
            new_index = new_index - 26

        result += ascii_lowercase[new_index]
    return result


def encrypt_v2(s, n):
    result = ""
    for c in s:
        result += ascii_lowercase[(ascii_lowercase.index(c) + n) % len(ascii_lowercase)]
    return result

print(encrypt_v2("zza", 1))
