
# Short Version
# Python 2.7

(n,k) = map(int,raw_input().split())

for i in range(n):
    l = raw_input().split()
    if 2*sum(map(int,l))<=k:
        print("YES")
        exit(0)

print("NO")

