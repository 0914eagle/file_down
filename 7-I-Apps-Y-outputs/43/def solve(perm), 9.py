
def solve(perm):
    # Write your code here
    n = len(perm)
    i = 0
    count = 0
    while i < n:
        j = i + 1
        while j < n:
            if perm[i] > perm[j]:
                break
            j += 1
        if j == n:
            count += 1
        i += 1
    return count

