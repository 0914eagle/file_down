
def find_kth_perfect(k):
    count = 0
    n = 0
    while count < k:
        n += 1
        if sum(map(int, str(n))) == 10:
            count += 1
    return n

k = int(input())
print(find_kth_perfect(k))

