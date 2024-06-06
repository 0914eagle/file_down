
n = int(input())
s = set()
for i in range(2**n):
    s.add(int(input()))
if 0 not in s:
    print("impossible")
    exit()
if 2**n-1 not in s:
    print("impossible")
    exit()
s.remove(0)
s.remove(2**n-1)
a = [0 for i in range(n)]
for i in s:
    for j in range(n-1,-1,-1):
        if 2**j+i in s:
            s.remove(2**j+i)
            a[j] += 1
            break
for i in a:
    print(i)
