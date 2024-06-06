
'''
k = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0
for i in range(n):
    if a[i] in b:
        c += 1
print(c)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0
for i in range(n):
    if a[i] in b:
        c += 1
print(c)

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0
for i in range(n):
    if a[i] in b:
        c += 1
print(c)
'''
b1, q, l, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
if b1 == 0 and q == 0:
    print("inf")
elif b1 == 0:
    if 0 in arr:
        print(0)
    else:
        print("inf")
elif b1 < 0:
    if q == 0:
        if 0 in arr:
            print(0)
        else:
            print("inf")
    elif q < 0:
        if 0 in arr:
            print(0)
        else:
            print("inf")
    else:
        if q >= l:
            if b1 > -l:
                print(1)
            else:
                print(0)
        else:
            if b1 > -l:
                print(1)
            else:
                print(0)
else:
    if q == 0:
        if 0 in arr:
            print(0)
        else:
            print("inf")
    elif q > 0:
        if 0 in arr:
            print(0)
        else:
            print("inf")
    else:
        if -q >= l:
            if b1 < l:
                print(1)
            else:
                print(0)
        else:
            if b1 < l:
                print(1)
            else:
                print(0)

