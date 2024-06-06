
n = int(input())

while n>0:
	s = input()
	s1 = input()
	s2 = input()
	n = n-3
	if len(s1)>1:
		s1 = s1[1:]
	if len(s2)>1:
		s2 = s2[:-1]
	if s1 != s2:
		print(0)
	else:
		print(1)
