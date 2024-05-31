
def inform_students(n, a):
    messages = []
    for i in range(2, n+1):
        if a[i-1] == 0:
            return -1
    
    for i in range(2, n+1):
        if a[i-1] > 0:
            messages.append((1, i))
            a[i-1] -= 1
    
    for i in range(2, n+1):
        for j in range(2, n+1):
            if i != j and a[i-1] > 0:
                messages.append((i, j))
                a[i-1] -= 1
    
    k = len(messages)
    print(k)
    for f, t in messages:
        print(f, t)

# Input
n = int(input())
a = list(map(int, input().split()))

# Output
inform_students(n, a)
