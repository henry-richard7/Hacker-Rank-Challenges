def diagonalDifference(arr):
    # Write your code here
    diagonal_1 = 0
    diagonal_2 = 0

    length_array = len(arr)
    for i in range(length_array):
        diagonal_1 += arr[i][i]
        diagonal_2 += arr[i][(length_array - 1) - i]
    return abs(diagonal_1 - diagonal_2)


n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
print(str(diagonalDifference(arr)))
