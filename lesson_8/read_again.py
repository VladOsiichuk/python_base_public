

file = open("sample.txt", "r")
data = file.read(5)
print(data)
data = file.read(5)
print(data)

print(file.read())
print("Finished reading the file. Try to read again...")
print(file.read())
file.close()
