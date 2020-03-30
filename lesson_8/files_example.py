def main():

    # Відкрити файл students.txt для запису. Якщо файл не знайдено,
    # то він буде створений автоматично
    file = open("students.txt", "w")
    student_names = "Vlad, \nVadym, \nVitaliy, \nEugen"

    # Записати у файл рядок
    file.write(student_names)

    # Закрити файл.
    file.close()


if __name__ == "__main__":
    main()
