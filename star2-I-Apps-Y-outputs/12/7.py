
n = int(input())
a = list(map(int, input().split()))

def reconstruct(n, a):
  students = [0] * n
  for i in range(n):
    students[a[i] - 1] = i + 1
  return students

print(*reconstruct(n, a))

