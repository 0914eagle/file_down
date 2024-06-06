
n = int(input())
a = list(map(int, input().split()))

a.sort()

i = 0
j = 1
while j < n:
    if a[j] - a[i] == a[i]:
        i += 1
        j += 1
    else:
        j += 1
print(i+1)
