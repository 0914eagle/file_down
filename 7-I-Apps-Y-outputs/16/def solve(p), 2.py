
def solve(p):
    # Your code goes here
    count = 0
    for i in range(1, len(p)-1):
        if p[i] == min(p[i-1], p[i+1]) and p[i] != min(p):
            count += 1
    return count

