
for _ in range(int(input())):
    n = int(input())
    print(n)
    print(*[i for i in range(n+1) if n%i==0])
