

from sys import stdin

a = list(map(int,stdin.readline().split()))

if a[0]+a[1]+a[2] == a[3]+a[4]+a[5]:
	print("YES")
elif a[0]+a[1]+a[3] == a[4]+a[5]+a[2]:
	print("YES")
elif a[0]+a[1]+a[4] == a[2]+a[3]+a[5]:
	print("YES")
elif a[0]+a[1]+a[5] == a[3]+a[4]+a[2]:
	print("YES")
elif a[0]+a[2]+a[3] == a[1]+a[4]+a[5]:
	print("YES")
elif a[0]+a[2]+a[4] == a[1]+a[3]+a[5]:
	print("YES")
elif a[0]+a[2]+a[5] == a[1]+a[3]+a[4]:
	print("YES")
elif a[0]+a[3]+a[4] == a[1]+a[2]+a[5]:
	print("YES")
elif a[0]+a[3]+a[5] == a[1]+a[2]+a[4]:
	print("YES")
elif a[0]+a[4]+a[5] == a[1]+a[2]+a[3]:
	print("YES")
else:
	print("NO")

