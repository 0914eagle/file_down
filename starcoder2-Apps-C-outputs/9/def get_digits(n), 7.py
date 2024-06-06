
def get_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits

def check(digits):
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            if digits[i] == digits[j]:
                return False
    return True

def solve(n):
    bills = []
    for i in range(1, n):
        for j in range(i + 1, n):
            if check(get_digits(i)) and check(get_digits(j)) and check(get_digits(i + j)):
                bills.append((i, j))
    return bills

n = int(input())
bills = solve(n)
print(len(bills))
for i in range(min(len(bills), 5000)):
    print(bills[i][0], bills[i][1])
