# as simple string
import json

def get_json_from_file():
    with open("test.json", "r") as f:
        result = json.loads(f.read())
    return result

d = get_json_from_file()
# d = {"1": 1}
print(type(d))
print(d)

key = input("new enter key   ")
pas = input("new enter pas   ")
d.update({key: pas})
# save(writen) in file
with open('test.json', 'w') as f:
    json.dump(d, f)

print(d)