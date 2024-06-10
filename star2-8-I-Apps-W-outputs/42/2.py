
def is_d_magic(num, d, m):
    i = 0
    while num:
        if num % 10 == d and i % 2 == 0:
            if num % m == 0:
                return True
            return False
        num //= 10
        i += 1
    return False


def find_num_d_magic(a, b, d, m):
    count = 0
    for num in range(a, b + 1):
        if is_d_magic(num, d, m):
            count += 1
    return count


m, d = map(int, input().split())
a = int(input())
b = int(input())
print(find_num_d_magic(a, b, d, m) % (10 ** 9 + 7))

