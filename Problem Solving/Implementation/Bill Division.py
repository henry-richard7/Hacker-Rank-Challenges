"""
bill -> arr
k -> value to skip
b -> Brian Charged Anna
"""


def bonAppetit(bill, k, b):
    bill.pop(k)
    total_cost = sum(bill) / 2

    if b > total_cost:
        return int(b - total_cost)
    else:
        return "Bon Appetit"


bonAppetit([3, 10, 2, 9], 1, 7)
