
from bisect import bisect_left
from collections import defaultdict

def solve():
	n = int(input())
	words = [input() for _ in range(n)]
	words_len = sum(len(word) for word in words)
	words_pos = [0]
	for word in words:
		words_pos.append(words_pos[-1] + len(word))
	words_pos_set = set(words_pos)
	q = int(input())
	for _ in range(q):
		t = int(input())
		if t == 1:
			p = input()
			pos = bisect_left(words_pos, 0)
			while pos < len(words_pos):
				if words_pos[pos] in words_pos_set:
					pos += 1
				else:
					break
			count = 0
			while pos < len(words_pos):
				if words_pos[pos] in words_pos_set:
					pos += 1
				else:
					break
				if p in words[pos - 1]:
					count += 1
			print(count)
		else:
			s = int(input())
			pos = bisect_left(words_pos, 0)
			while pos < len(words_pos):
				if words_pos[pos] in words_pos_set:
					pos += 1
				else:
					break
			count = 0
			while pos < len(words_pos):
				if words_pos[pos] in words_pos_set:
					pos += 1
				else:
					break
				if p in words[pos - 1]:
					count += 1
			print(count)

solve()

