
import math

def is_valid(num):
    digits = set()
    while num:
        digits.add(num % 10)
        num //= 10
    return len(digits) == 3

def is_valid_bill(bev, main):
    return is_valid(bev) and is_valid(main) and bev < main

def solve(price):
    bills = set()
    for bev in range(1, math.ceil(price / 2)):
        main = price - bev
        if is_valid_bill(bev, main):
            bills.add((bev, main))
    return bills

def main():
    price = int(input())
    bills = solve(price)
    print(len(bills))
    for bev, main in sorted(bills)[:5000]:
        print(bev, main)

if __name__ == '__main__':
    main()
