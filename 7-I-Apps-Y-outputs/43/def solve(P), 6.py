
def solve(P):
    # Write your code here
    count = 0
    for i in range(len(P)):
        for j in range(i):
            if P[i] < P[j]:
                break
        else:
            count += 1
    return count

