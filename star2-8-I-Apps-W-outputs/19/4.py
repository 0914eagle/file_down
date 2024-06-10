
from collections import defaultdict
def solve(s):
	s_len = len(s)
	counts = defaultdict(int)
	for c in s:
		if c != '?':
			counts[c] += 1
	missing_chars = 26 - len(counts)
	if missing_chars > s_len - 26:
		return '-1'
	missing_letters = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ') - set(counts.keys())
	res = ''
	for c in s:
		if c == '?':
			res += missing_letters.pop()
		else:
			res += c
	return res
s = input().strip()
print(solve(s))

