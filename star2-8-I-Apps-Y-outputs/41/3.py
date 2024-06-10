
n, k = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
letters = [chr(i) for i in range(97, 97+k)]
s = ['a'] * n
for i in range(n):
    s[p[i]-1] = letters[i%k]
for i in range(n):
    if s[q[i]-1] != letters[i%k]:
        s[q[i]-1] = letters[i%k]
print("YES")
print("".join(s))

