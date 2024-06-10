
k = int(input())

def is_perfect(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s == 10

c = 0
n = 0
while c < k:
    n += 1
    if is_perfect(n):
        c += 1
print(n)

