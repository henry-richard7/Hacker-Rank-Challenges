def miniMaxSum(arr):
    sums = []
    total = 0
    for i in range(len(arr)):
        total = 0
        for j in range(len(arr)):
            if j != i:
                total += arr[j]
        sums.append(total)
        total = 0
    print(sorted(sums)[0], sorted(sums)[len(sums) - 1])


arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)
