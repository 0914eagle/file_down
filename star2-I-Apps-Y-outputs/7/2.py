
n, q = map(int, input().split())
a = list(map(int, input().split()))
b = [int(input()) for _ in range(q)]

def solve(a, b):
    a.sort()
    for i in range(q):
        if b[i] in a:
            print(1)
        elif b[i] % 2 == 1:
            print(-1)
        else:
            cnt = 0
            while b[i] > 0:
                if b[i] in a:
                    print(cnt + 1)
                    break
                else:
                    b[i] //= 2
                    cnt += 1
            else:
                print(-1)

solve(a, b)

