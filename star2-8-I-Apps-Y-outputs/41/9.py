
n, k = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

s = ""
for i in range(k):
    s += chr(ord('a') + i)
for i in range(k, n):
    s += s[0]

print("YES")
print(s)

