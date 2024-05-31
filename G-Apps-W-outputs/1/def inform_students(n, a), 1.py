
def inform_students(n, a):
    messages = []
    for i in range(n):
        if a[i] == 0 and i != 0:
            return -1
        if a[i] > 0:
            messages.append((1, i+1))
            a[i] -= 1
    
    for i in range(n):
        for j in range(n):
            if a[i] > 0 and a[j] > 0 and i != j:
                messages.append((i+1, j+1))
                a[i] -= 1
                a[j] -= 1
                if a[i] == 0:
                    break
    
    if any(x > 0 for x in a):
        return -1
    
    print(len(messages))
    for msg in messages:
        print(msg[0], msg[1])

# Input parsing
n = int(input())
a = list(map(int, input().split()))

inform_students(n, a)
