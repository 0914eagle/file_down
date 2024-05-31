
def inform_students(n, a):
    messages = []
    for i in range(2, n+1):
        if a[i-1] == 0:
            print(-1)
            return
        for _ in range(a[i-1]):
            messages.append((1, i))
            if len(messages) >= n-1:
                break
    print(len(messages))
    for message in messages:
        print(message[0], message[1])

# Input
n = int(input())
a = list(map(int, input().split()))

# Call the function
inform_students(n, a)
