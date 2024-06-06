
# bai 1
# hàm in hoán vị
# 
def permutation(n, a):
    if n == 1:
        print(a)
    else:
        for i in range(n-1):
            if i != 0 and a[i] == a[0]:
                continue
            a[0], a[i] = a[i], a[0]
            permutation(n-1, a[1:])
            a[0], a[i] = a[i], a[0]
a = list(map(int,input().split()))
permutation(len(a), a)

# bai 2
# hàm này là hàm thay đổi giá trị của 2 số tại vị trí x và y
def swap(a,x,y):
    tmp = a[x]
    a[x] = a[y]
    a[y] = tmp
# hàm in hoán vị
def permutation(n, a):
    if n == 1:
        print(a)
    else:
        for i in range(n-1):
            if i != 0 and a[i] == a[0]:
                continue
            swap(a,0,i)
            permutation(n-1, a[1:])
            swap(a,0,i)
a = list(map(int,input().split()))
permutation(len(a), a)
