

def solve(s):
	stack = []
	pos = []
	for i, ch in enumerate(s):
		if ch == "(":
			stack.append(ch)
			pos.append(i)
		elif ch == ")":
			if len(stack) == 0:
				return "invalid"
			stack.pop()
			pos.pop()
	if len(stack) != 0:
		return "invalid"
	res = ""
	pos_stack = []
	for i in range(len(pos)):
		pos_stack.append(pos[i])
		pos_stack.append(pos[-i-1])
		res += str(pos_stack[-2]) + "," + str(pos_stack[-1]) + ":"
	return res[:-1]

s = input()
print(solve(s))


