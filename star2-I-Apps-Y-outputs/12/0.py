
n = int(input())
a = list(map(int, input().split()))

students = [0] * (n + 1)
for i, x in enumerate(a, 1):
    students[x] = i

print(*students[1:])

