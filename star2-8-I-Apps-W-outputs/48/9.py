
n = int(input())
def perfect(x):
    s = 0
    for c in str(x):
        s += int(c)
    return s == 10
def find_kth_perfect(k):
    x = 1
    cnt = 0
    while cnt < k:
        if perfect(x):
            cnt += 1
        x += 1
    return x - 1
print(find_kth_perfect(n))

