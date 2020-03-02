columns = int(input("Введіть к-сть стовпчиків матриці: "))
rows = int(input("Введіть к-сть рядків: "))

matrix = []
for row_index in range(columns):
    matrix.append(list())
    for column_index in range(rows):
        print(row_index, column_index)
        value = int(input(f"Введіть значення [{row_index}][{column_index}]: "))
        matrix[row_index].append(value)

# for i in range(0, rows):
#     print(matrix[i])
# print(matrix)
for row in matrix:
    print(row)
    for row_value in row:
        print(row_value, end=" ")
    print()
