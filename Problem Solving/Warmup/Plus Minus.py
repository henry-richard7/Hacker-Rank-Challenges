def plusMinus(arr, n):
    no_negative_values = 0
    no_positive_values = 0
    no_zeros = 0

    for i in range(n):
        if arr[i] > 0:
            no_positive_values += 1
        elif arr[i] < 0:
            no_negative_values += 1
        else:
            no_zeros += 1

    print("{:6f}".format(no_positive_values / n))
    print("{:6f}".format(no_negative_values / n))
    print("{:6f}".format(no_zeros / n))


n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
plusMinus(arr, n)
