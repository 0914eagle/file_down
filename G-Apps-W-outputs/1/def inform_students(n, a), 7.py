
def inform_students(n, a):
    messages = []
    for i in range(1, n):
        if a[i] == 0:
            return -1
        messages.append((1, i+1))
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and a[i-1] > 0 and a[j-1] > 0:
                messages.append((i, j))
                a[i-1] -= 1
                a[j-1] -= 1
                if sum(a) == 0:
                    return len(messages), messages
    return -1

# Input
n = int(input())
a = list(map(int, input().split()))

# Output
result = inform_students(n, a)
if result == -1:
    print(-1)
else:
    k, messages = result
    print(k)
    for f, t in messages:
        print(f, t)
