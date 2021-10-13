def compareTriplets(a, b):
    # Write your code here
    alice_points = 0
    bob_points = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alice_points += 1
        elif a[i] < b[i]:
            bob_points += 1
    return alice_points, bob_points


a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)
print(' '.join(map(str, result)))
