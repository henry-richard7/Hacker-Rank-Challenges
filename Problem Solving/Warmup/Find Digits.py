"""
Find Digits
"""


def check_divisibility(n):
    count = 0

    for i in str(n):
        if int(i) != 0:
            if n % int(i) == 0:
                count += 1
    return count


read_line = int(input())

for i in range(read_line):
    n = int(input())
    print(check_divisibility(n))
