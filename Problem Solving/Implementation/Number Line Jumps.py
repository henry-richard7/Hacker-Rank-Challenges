def kangaroo(x1, v1, x2, v2):
    v_diff = v1 - v2
    x_diff = x1 - x2

    if v_diff <= 0:
        return "NO"
    elif x_diff % v_diff == 0:
        return "YES"
    else:
        return "NO"


first_multiple_input = input().rstrip().split()

x1 = int(first_multiple_input[0])

v1 = int(first_multiple_input[1])

x2 = int(first_multiple_input[2])

v2 = int(first_multiple_input[3])

result = kangaroo(x1, v1, x2, v2)

print(result)
