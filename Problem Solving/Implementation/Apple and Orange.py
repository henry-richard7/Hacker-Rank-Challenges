"""
    Range should be s - t
    a -> Apple Location
    b -> Orange Location
    m -> total apples
    n -> total oranges
    """


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_position = []
    oranges_position = []

    for apple in apples:
        apples_position.append(a + apple)

    for orange in oranges:
        oranges_position.append(b + orange)

    apple_count = 0
    orange_count = 0

    for apple_position in apples_position:
        if s <= apple_position <= t:
            apple_count += 1

    for orange_position in oranges_position:
        if s <= orange_position <= t:
            orange_count += 1

    print(apple_count)
    print(orange_count)


first_multiple_input = input().rstrip().split()

s = int(first_multiple_input[0])

t = int(first_multiple_input[1])

second_multiple_input = input().rstrip().split()

a = int(second_multiple_input[0])

b = int(second_multiple_input[1])

third_multiple_input = input().rstrip().split()

m = int(third_multiple_input[0])

n = int(third_multiple_input[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)
