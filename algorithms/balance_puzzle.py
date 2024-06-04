#!/usr/bin/python

def balance_puzzle(coins, index=0):
    length = len(coins)
    if length <= 1:
        return index
    
    def the_part_nobody_cares_about(length):
        remainder = length % 3
        def aux(remainder): return remainder if remainder < 2 else -1

        n0 = 0
        n1 = int(((length - aux(remainder)) / 3))
        n2 = int(2 * int((length - aux(remainder)) / 3))
        return n0, n1, n2

    n0, n1, n2 = the_part_nobody_cares_about(length)

    if sum(coins[:n1]) > sum(coins[n1:n2]):
        return balance_puzzle(coins[:n1], index + n0)
    elif sum(coins[:n1]) < sum(coins[n1:n2]):
        return balance_puzzle(coins[n1:n2], index + n1)
    elif sum(coins[:n1]) == sum(coins[n1:n2]):
        return balance_puzzle(coins[n2:], index + n2)



coins = [100, 100, 100, 100, 100, 100, 100, 100, 101]
a = balance_puzzle(coins)
print(type(a))
print(a)