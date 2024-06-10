
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

def solve(a):
    if len(a) % 2 == 1:
        return -1
    
    stack = []
    for x in a:
        if x > 0:
            stack.append(x)
        else:
            if not stack or stack[-1] != -x:
                return -1
            stack.pop()
    
    return 1

def main():
    res = solve(a)
    if res == -1:
        print(res)
    else:
        print(res)
        print(len(a))

main()

