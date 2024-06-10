
n, k = map(int, input().split())
s = ""
for i in range(k):
    s += "1"
for i in range(n - k):
    s += "0"
print(s)

