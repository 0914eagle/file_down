
n = int(input())
a = list(map(int, input().split()))

students = [0] * n
for i in range(n):
    students[a[i] - 1] = i + 1

print(*students)

