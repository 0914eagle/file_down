
#code
import sys
line = sys.stdin.readline().split()
n = int(line[0])
m = int(line[1])
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
a.sort()
b.sort(reverse=True)
print(a[0]*b[0])
