
n = int(input())
s = input()

count = n

for i in range(1, n):
	if s[i] == s[i-1]:
		break

count = count + (n - i)

print(count)
