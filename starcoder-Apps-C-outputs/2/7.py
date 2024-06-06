
import random 
import math

def expected(n,d,c,l1,l2):
	l = [i for i in range(1,n+1)]
	m = 0
	for i in range(1,10000):
		l = [i for i in range(1,n+1)]
		while True:
			m+=1
			l3 = random.sample(l,d)
			l = [j for j in l if j not in l3]
			if len(l3) != 0 and l3[0] in l1:
				return m/i
			elif len(l3) != 0 and l3[0] in l2:
				return m/i
			else:
				continue
	return m/10000
