
def lineup(n, d):
    # Write your code here
    for i in range(n-1):
        d[i+1] += d[i] + 1
    return d

