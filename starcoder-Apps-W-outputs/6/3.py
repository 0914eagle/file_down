
n = int(input())
s = input()
ans = 0
for i in range(n):
    ans += s.count('(') - s.count(')')
print(ans)
