arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]
max = arr[0][0]
min = arr[0][0]

max_indexes = (0, 0)
min_indexes = (0, 0)

for i, row in enumerate(arr):
    for j, value in enumerate(row):
        if value > max:
            max = value
            max_indexes = (i, j)
        if value < min:
            min = value
            min_indexes = (i, j)

print(max, min, max_indexes, min_indexes)
