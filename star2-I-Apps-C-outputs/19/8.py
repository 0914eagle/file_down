
import sys

def solve(n, C, p, b, u):
    users = [(p[i], b[i], u[i]) for i in range(n)]
    users.sort()
    
    buffer = [0] * n
    for i in range(n):
        buffer[i] = b[i] - (p[i] + C)
    
    total_upload = 0
    for i in range(n):
        if total_upload + u[i] <= C:
            total_upload += u[i]
        else:
            break
    
    if total_upload == C:
        return max(buffer)
    
    for j in range(i, n):
        if total_upload + u[j] <= C:
            total_upload += u[j]
            buffer[j] += total_upload - C
        else:
            buffer[j] += C - total_upload
            break
    
    return max(buffer)

def main():
    n, C = map(int, sys.stdin.readline().split())
    
    p = [0] * n
    b = [0] * n
    u = [0] * n
    
    for i in range(n):
        p[i], b[i], u[i] = map(int, sys.stdin.readline().split())
    
    print(solve(n, C, p, b, u))

if __name__ == "__main__":
    main()

