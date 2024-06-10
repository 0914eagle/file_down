
def read_int():
    return int(input())

def read_ints():
    return [int(x) for x in input().split()]

def get_row_nums(n):
    res = [0] * (n + 1)
    res[1] = 1
    for i in range(2, n + 1):
        res[i] = res[i - 1] + res[i - 1] % 10 + 1
    return res

def count_nums(a, b):
    res = 0
    for n in range(a, b + 1):
        res += get_row_nums(n)[-1]
    return res

q = read_int()
for _ in range(q):
    a, b = read_ints()
    print(count_nums(a, b))

