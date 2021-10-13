import math


def getTotalX(a, b):
    lcm = math.lcm(*a)
    gcd = math.gcd(*b)
    total_sum = 0
    factors_a1 = []
    for i in range(1, gcd + 1):
        if i % lcm == 0:
            factors_a1.append(i)

    for i in range(lcm, gcd + 1, lcm):
        if gcd % i == 0:
            total_sum += 1

    return total_sum


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

brr = list(map(int, input().rstrip().split()))

total = getTotalX(arr, brr)

print(total)
