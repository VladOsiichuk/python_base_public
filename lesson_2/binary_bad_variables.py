a = int(input("Enter a: "))
s = ""

while a > 0:
    s += str(a % 2)
    a //= 2

s = s[::-1]
print(s)