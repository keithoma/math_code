def the_part_nobody_cares_about(length):
    remainder = length % 3
    def aux(remainder): return remainder if remainder < 2 else -1

    n0 = 1
    n1 = int(((length - aux(remainder)) / 3)) + 1
    n2 = int(2 * int((length - aux(remainder)) / 3)) + 1
    return n0, n1, n2

print(the_part_nobody_cares_about(5))