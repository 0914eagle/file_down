
from collections import defaultdict
def solve(s):
	s = list(s)
	letters = defaultdict(int)
	for c in s:
		if c != "?":
			letters[c] += 1
	for i in range(len(s)):
		if s[i] == "?":
			for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
				if letters[c] == 0:
					s[i] = c
					letters[c] += 1
					break
			if s[i] == "?":
				return -1
	if len(letters) == 26:
		return "".join(s)
	return -1
s = input()
print(solve(s))

