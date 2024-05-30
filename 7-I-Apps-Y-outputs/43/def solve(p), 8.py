
def solve(p):
    # Your code goes here
    n = len(p)
    count = 0
    for i in range(1, n+1):
        flag = True
        for j in range(1, i+1):
            if p[i-1] < p[j-1]:
                flag = False
                break
        if flag:
            count += 1
    return count

