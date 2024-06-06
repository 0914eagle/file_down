
n, x, k = list(map(int, input().split()))
l = list(map(int, input().split()))
# print(n, x, k)
# print(l)
count = 0
for i in range(n):
	for j in range(i,n):
		# print(i, j)
		# print(l[i], l[j])
		if l[i] <= l[j] and k >= (l[j]-l[i])//x:
			count += 1
print(count)
