
for _ in range(int(input())):
    n = int(input())
    print(n)
    for i in range(n+1):
        if n%i == 0:
            print(i, end=' ')
    print()
