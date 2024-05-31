
def inform_students(n, a):
    messages = []
    for i in range(1, n):
        if a[i] == 0:
            return -1
        messages.append((1, i+1))
    
    for i in range(1, n):
        for j in range(i+1, n):
            if a[j] > 0:
                messages.append((i+1, j+1))
                a[j] -= 1
                if a[j] == 0:
                    break
    
    return len(messages), messages

# Input parsing
n = int(input())
a = list(map(int, input().split()))

result = inform_students(n, a)

if result == -1:
    print(-1)
else:
    print(result[0])
    for message in result[1]:
        print(message[0], message[1])
