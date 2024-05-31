
def inform_students(n, a):
    messages = []
    
    for i in range(1, n):
        informed = False
        for j in range(1, n):
            if a[j] > 0:
                messages.append((j, i+1))
                a[j] -= 1
                informed = True
                break
        
        if not informed:
            return -1
    
    return len(messages), messages

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
