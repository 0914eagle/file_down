
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = []

for i in range(n):
	s.append([a[i],b[i]])

k = 0
t = 0
for i in range(n):
	k = k + s[i][0] // s[i][1]
	t = t + s[i][0] // s[i][1]
	s[i][0] = s[i][0] % s[i][1]
	if s[i][0] == 0:
		s[i][1] = 1000
	else:
		k = k + 1

for i in range(n):
	t = t + min(s[i][0], s[i][1] - s[i][0])

print(k, t)
