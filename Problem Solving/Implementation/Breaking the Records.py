def breakingRecords(scores):
    count_high = 0
    count_low = 0

    current_high = scores[0]
    current_low = scores[0]

    for i in range(1, len(scores)):
        if scores[i] < current_low:
            count_low += 1
            current_low = scores[i]

        if scores[i] > current_high:
            count_high += 1
            current_high = scores[i]

    return count_high, count_low


n = int(input().strip())

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)

print(' '.join(map(str, result)))
