
def inform_students(n, a):
    messages = []
    for i in range(1, n):
        if a[i] == 0:
            return -1
        messages.append((1, i+1))
        a[i] -= 1
        a[0] -= 1
        while a[i] > 0 and a[0] > 0:
            max_a = max(a)
            max_index = a.index(max_a)
            messages.append((i+1, max_index+1))
            a[max_index] -= 1
            a[0] -= 1
    return len(messages), messages

# Input
n = int(input())
a = list(map(int, input().split()))

# Output
result = inform_students(n, a)
if result == -1:
    print(-1)
else:
    print(result[0])
    for message in result[1]:
        print(message[0], message[1])
