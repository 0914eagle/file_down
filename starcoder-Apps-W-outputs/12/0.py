
# The first line of input will contain three space separated integers n (1 ≤ n ≤ 2·10^5), t (0 ≤ t ≤ 10^9) and c (1 ≤ c ≤ n). The next line will contain n space separated integers, the i^{th} integer is the severity i^{th} prisoner's crime. The value of crime severities will be non-negative and will not exceed 10^9. 
a = raw_input()
a = a.split()
n = int(a[0])
t = int(a[1])
c = int(a[2])
b = raw_input()
b = b.split()
count = 0
for i in range(n):
	if (int(b[i])<=t):
		count = count + 1
	else:
		break
for i in range(n-1,n-c-1,-1):
	if(int(b[i])<=t):
		count = count + 1
	else:
		break
print count
