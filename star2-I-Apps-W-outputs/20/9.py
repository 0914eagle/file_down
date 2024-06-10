
n = int(input())
a = list(map(int, input().split()))

def solve(a):
    stack = []
    for i in range(len(a)):
        if a[i] > 0:
            stack.append(a[i])
        else:
            if len(stack) == 0 or stack[-1] != -a[i]:
                return -1
            stack.pop()
    return len(stack)

print(solve(a))

