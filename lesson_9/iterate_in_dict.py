people_years = {"Andriy": 18, "Olena": 22, "Iryna": 19}

for key in people_years:
    print(key)

for value in people_years.values():
    print(value)

for name, year in people_years.items():
    print(f"{name} is {year} years old")
