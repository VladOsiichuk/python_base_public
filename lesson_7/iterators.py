s = "abcdefghq123123"

s.upper()  # This is not correct
s = s.upper()  # This is correct

s[2] = "w"

for i in range(len(s)):
    if s[i].isalpha():
        print(s[i], end="")

print()

for c in s:
    if c.isalpha():
        print(c, end="")
print()
