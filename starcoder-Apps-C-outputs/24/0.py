
for i in range(n):
	for j in range(n):
		if a[i][j] == 'E':
			cnt += 1
			if cnt > n:
				print -1
				exit(0)
