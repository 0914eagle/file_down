
def inform_students(n, a):
    messages = []
    for i in range(1, n):
        if a[i] == 0:
            return -1
        for j in range(min(a[i], n-1)):
            messages.append((i+1, (i+j)%n+1))
    
    print(len(messages))
    for message in messages:
        print(message[0], message[1])

# Input parsing
n = int(input())
a = list(map(int, input().split()))

# Call the function with input values
inform_students(n, a)
