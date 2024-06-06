
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a = [a[i]-b[i] for i in range(n)]
i = 0
j = 0
t = 0
k = 0
soda = 0
while i < n:
    while j < n and a[j] <= 0:
        j += 1
    if j >= n:
        break
    soda += a[j]
    a[j] = 0
    t = 0
    k += 1
    while soda >= 0:
        j = 0
        t += 1
        while j < n and soda >= 0:
            if a[j] > 0:
                soda -= b[j]
                a[j] = 0
            j += 1
    soda = 0
    i += 1
print(k, t)
