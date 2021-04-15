def seven():
    listi = []
    for x in range(1000, 9999):
        if x % 7 == 0:
            # print("{} is divisible by 7!".format(x))
            a = x % 10
            b = ((x - a) % 100) / 10
            c = ((x - a - b * 10) % 1000) / 100
            d = (x - a - b * 10 - c * 100) / 1000

            y = int(b + a * 10 + c * 100 + d * 1000)

            # print("x = {} || y = {}".format(x, y))

            if y % 7 == 0 and d == 8:
                listi.append([x, y])

    return listi

def test():
    x = 1234
    a = x % 10
    b = ((x - a) % 100) / 10
    c = ((x - a - b * 10) % 1000) / 100
    d = ((x - a - b * 10 - c * 100)) / 1000

    print(a)
    print(b)
    print(c)
    print(d)

    y = int(b + a * 10 + c * 100 + d * 1000)

    print(y)

def main():
    print(seven())
    print(len(seven()))
    # test()

if __name__ == "__main__":
    main()
