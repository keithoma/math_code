import random

class CouponCollector():
    def __init__(self, n, m):
        self.n = n # number of coupons to collect
        self.m = m # number of copies to collect
        self.collection = [0 for _ in range(n)]
    
    def add_coupon(self):
        index = random.randint(0, self.n - 1)
        self.collection[index] += 1

    def completed(self):
        for coupon in self.collection:
            if coupon < self.m:
                return False
        return True

    def add_until_completion(self):
        added = 0
        while True:
            added += 1
            self.add_coupon()
            if self.completed():
                self.collection = [0 for _ in range(self.n)]
                return added

    def average_added(self, tries):
        list_of_tries = []
        for _ in range(tries):
            current = self.add_until_completion()
            list_of_tries.append(current)
            print("{}th try, {} coupons added".format(_, current))
            print("the average currently is: {}".format(sum(list_of_tries) / len(list_of_tries)))
            print()



def main():
    obj = CouponCollector(552, 2)
    obj.average_added(10000000)

if __name__ == "__main__":
    main()