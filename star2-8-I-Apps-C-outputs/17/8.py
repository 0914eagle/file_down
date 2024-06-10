
def get_input():
    n, k = input().split()
    return int(n), int(k)


def get_string(n, k):
    res = ''
    for i in range(n):
        if i < k:
            res += '1'
        else:
            res += '0'
    return res


n, k = get_input()
print(get_string(n, k))

