
k = int(input())
def is_perfect(n):
    return sum(map(int, str(n))) == 10

def kth_perfect(k):
    perfect = 0
    i = 0
    while perfect < k:
        i += 1
        if is_perfect(i):
            perfect += 1
    return i
print(kth_perfect(k))

