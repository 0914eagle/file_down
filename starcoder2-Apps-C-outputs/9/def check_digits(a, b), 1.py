
import math

def check_digits(a, b):
    a = str(a)
    b = str(b)
    for i in a:
        if i in b:
            return False
    return True

def check_price(a, b, c):
    if a + b == c:
        return True
    return False

def check_order(a, b):
    if a < b:
        return True
    return False

def check_bill(a, b, c):
    if check_digits(a, b) and check_digits(a, c) and check_digits(b, c) and check_price(a, b, c) and check_order(a, b):
        return True
    return False

def check_bill_list(a, b, c, bill_list):
    for i in bill_list:
        if a == i[0] and b == i[1]:
            return False
    return True

def get_bill_list(a, b, c):
    bill_list = []
    for i in range(1, a):
        for j in range(1, b):
            if check_bill(i, j, c):
                if check_bill_list(i, j, c, bill_list):
                    bill_list.append([i, j])
    return bill_list

def print_bill_list(bill_list):
    print(len(bill_list))
    for i in bill_list:
        print(i[0], i[1])

if __name__ == "__main__":
    price = int(input())
    bill_list = get_bill_list(price, price, price)
    print_bill_list(bill_list)
