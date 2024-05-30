
import collections
N = int(input())
l = input().split()
marks = []
for i in range(N):
    x = input().split()
    marks.append(int(x[1]))
print("{:.2f}".format(sum(marks)/N))

