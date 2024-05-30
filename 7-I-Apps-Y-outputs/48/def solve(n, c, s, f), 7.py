

def solve(n, c, s, f):
    # Write your code here
    time = 0
    for i in range(1, n):
        time += s[i-1]
        time += c[i-1]
        time += f[i-1] - (time % f[i-1])
    return time

