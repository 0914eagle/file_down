
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    if n == 1:
        print(0)
    elif n == 2:
        print(m)
    else:
        if n % 2 == 0:
            print(2*m)
        else:
            print(2*m)
            
