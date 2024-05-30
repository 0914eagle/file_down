
def solve(N, P):
    # Write your code here
    count = 0
    for i in range(1, N+1):
        flag = True
        for j in range(1, i+1):
            if P[i-1] < P[j-1]:
                flag = False
                break
        if flag:
            count += 1
    return count

