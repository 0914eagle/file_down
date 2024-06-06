
def check_is_regular(s):
	stack = []
	for c in s:
		if c == ')':
			if len(stack) == 0:
				return False
			stack.pop()
		else:
			stack.append(c)
	return len(stack) == 0
n = int(input())
s = []
for _ in range(n):
	s.append(input())
ans = 0
for i in range(n):
	for j in range(i + 1):
		if check_is_regular(s[i] + s[j]):
			ans += 1
print(ans)
