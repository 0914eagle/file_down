
def solve_credit_info(n, a):
    messages = []
    for i in range(1, n):
        if a[i] == 0:
            return -1

    for i in range(1, n):
        for j in range(a[i]):
            messages.append((i, i+1))
    
    print(len(messages))
    for m in messages:
        print(m[0], m[1])

# Input
n = int(input())
a = list(map(int, input().split()))

# Solve
solve_credit_info(n, a)
