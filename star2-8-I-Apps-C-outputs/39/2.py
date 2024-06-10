
from sys import stdin
input()
a = sorted(map(int, stdin.readline().split()))

count = 0
for i in range(len(a) - 2):
    left, right = i + 1, len(a) - 1
    while left < right:
        s = a[i] + a[left]
        if s == a[right]:
            count += 1
            left += 1
            right -= 1
        elif s < a[right]:
            right -= 1
        else:
            left += 1

print(count)

