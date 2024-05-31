
def inform_students(n, a):
    messages = []
    
    for i in range(1, n):
        if a[i] == 0:
            return -1
        else:
            messages.append((1, i+1))
    
    for i in range(1, n):
        for j in range(i+1, n):
            if a[i] > 0 and a[j] > 0:
                messages.append((i+1, j+1))
    
    return len(messages), messages

# Read input
n = int(input())
a = list(map(int, input().split()))

# Call the function and print the output
result = inform_students(n, a)
if result == -1:
    print(-1)
else:
    k, messages = result
    print(k)
    for message in messages:
        print(message[0], message[1])
