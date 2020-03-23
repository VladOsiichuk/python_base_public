def main():
    people_years = {"Andriy": 18, "Olena": 22, "Iryna": 19}

    # Пошук ключів можна створювати за допомогою оператора in
    print("Olena" in people_years)

    # У словниках є також метод .pop()
    # В даний метод можна передавати два аргументи
    # Перший аргумент вказує на ключ, другий, означає значення,
    # яке буде повернуто, якщо такого ключа не існує
    year = people_years.pop("Andriy", "not found")
    print(f"Year of Andriy: {year}")
    year = people_years.pop("Vasyl", "not found")
    print(year)

    # Поміняти значення в словнику можна через ключ
    people_years["Andriy"] = 19

    # А можна і через метод .update()
    people_years.update({"Olena": 23, "Vasyl": 35})


if __name__ == "__main__":
    main()
