"""
Extra Long Factorials
"""


def extraLongFactorials(n):
    result = 1
    for i in range(1, n + 1):
        print(i)
        result *= i

    print(result)


extraLongFactorials(25)
