
#https://codeforces.com/contest/1076/problem/B

n=int(input())

if n == 1:
    print("1")
elif n < 1:
    print("-1")
else:
    while n % 2 == 0:
        n /= 2
    if n == 1:
        print("2")
    else:
        print("1")

