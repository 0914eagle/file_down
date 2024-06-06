
n = int(input())
l = list(map(int, input().split()))
count = 0
for i in range(1, n):
    count += abs(l[i] - l[i - 1])
print(count)
