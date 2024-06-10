
import sys
import math
def solve():
	a,b,c = map(int,input().split())
	m = int(input())
	mouses = [list(input().split()) for _ in range(m)]
	usb = [int(x) for x,y in mouses if y == "USB"]
	ps2 = [int(x) for x,y in mouses if y == "PS/2"]
	usb.sort()
	ps2.sort()
	i = 0
	j = 0
	cost = 0
	while i < len(usb) and j < a:
		cost += usb[i]
		i += 1
		j += 1
	i = 0
	while i < len(ps2) and j < b+a:
		cost += ps2[i]
		i += 1
		j += 1
	i = 0
	while i < len(ps2) and j < b+a+c:
		cost += ps2[i]
		i += 1
		j += 1
	print(j,cost)
solve()

