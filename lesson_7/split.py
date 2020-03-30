arr = "good. I will come. wait".split(".")

print(arr)

# arr = list(map(str.strip, arr))
# print(arr)
arr = "good. I will come. wait".split(". ")
print(arr)

s = ", ".join(["1", "2", "3"])
print(s)
s = ", ".join(arr)
print(s)

# Поміняти символи
s = "12345a, asd, a234"
s = s.replace(",", "")
print(s)
