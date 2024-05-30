
def lineup(n, d):
    # write your code here
    return [1] + [i for i in range(2, n+1) for _ in range(d[i-1])]

