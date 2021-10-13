ar_count = int(input().strip())

ar = list(map(int, input().rstrip().split()))


def simpleArraySum(ar):
    total = 0
    for num in ar:
        total += num
    return total


print(simpleArraySum(ar))
