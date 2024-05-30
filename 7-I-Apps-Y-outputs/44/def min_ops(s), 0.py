
def min_ops(s):
    n = len(s)
    a_count = 0
    b_count = 0
    min_ops = 0
    for i in range(0, n, 2):
        if s[i] == 'a':
            a_count += 1
        else:
            b_count += 1
    if a_count != b_count:
        min_ops = abs(a_count - b_count)
    for i in range(1, n, 2):
        if s[i] == 'a':
            a_count -= 1
        else:
            b_count -= 1
        if a_count != b_count:
            min_ops += abs(a_count - b_count)
    return min_ops


def modify(s):
    n = len(s)
    a_count = 0
    b_count = 0
    for i in range(0, n, 2):
        if s[i] == 'a':
            a_count += 1
        else:
            b_count += 1
    if a_count != b_count:
        for i in range(0, n, 2):
            if s[i] == 'a':
                s[i] = 'b'
                break
            else:
                s[i] = 'a'
                break
    for i in range(1, n, 2):
        if s[i] == 'a':
            a_count -= 1
        else:
            b_count -= 1
        if a_count != b_count:
            for i in range(1, n, 2):
                if s[i] == 'a':
                    s[i] = 'b'
                    break
                else:
                    s[i] = 'a'
                    break
    return s


n = int(input())
s = list(input())
min_ops_count = min_ops(s)
print(min_ops_count)
print(''.join(modify(s)))

