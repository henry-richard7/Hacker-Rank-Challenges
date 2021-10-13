def aVeryBigSum(ar):
    total = 0
    for num in ar:
        total += num
    return total


ar_count = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(ar)
print(str(result))
