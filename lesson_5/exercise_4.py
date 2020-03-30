arr = [2, 3, 1, 10, 8, 4]
# arr = [2, 3, 1, 10, 8, 4]
# arr = [2, 1, 3, 10, 8, 4]
# arr = [2, 1, 3, 10, 8, 4]
# arr = [2, 1, 3, 8, 10, 4]
# arr = [2, 1, 3, 8, 4, 10]
# arr = [1, 2, 3, 8, 4, 10]

# arr = [1, 2, 3, 4, 8, 10] 

n = 0
while True:
    array_is_sorted = True

    if arr[n] > arr[n + 1]:
        arr[n], arr[n+1] = arr[n+1], arr[n]
    
    n += 1
    if n+1 == len(arr):
        n = 0

    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            array_is_sorted = False
            break

    if array_is_sorted:
        break


# for i in range(len(arr)-1):
#     if arr[i] > arr[i+1]:
#         arr[i], arr[i+1] = arr[i+1], arr[i]
print(arr)