def migratoryBirds(arr):
    count = [0] * 6
    for t in arr:
        count[t] += 1
    return count.index(max(count))


arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = migratoryBirds(arr)
print(result)
