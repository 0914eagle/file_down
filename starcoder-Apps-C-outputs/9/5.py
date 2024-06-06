
def soda(n,a,b):
	a = sorted(a)
	b = sorted(b)
	s = 0
	t = 0
	i = n - 1
	for j in range(n - 1, -1, -1):
		while b[j] < a[i]:
			s += 1
			b[j] += b[j+1]
		t += a[i]
		i -= 1
	return s,t
print(soda(4,[3,3,4,3],[4,7,6,5]))
