
n = int(input())
p = list(map(int, input().split()))

def solve(p):
    sorted_p = sorted(p)
    l = 0
    r = n - 1
    count = 0
    while l < n:
        if p[l] == sorted_p[l]:
            l += 1
        elif p[r] == sorted_p[l]:
            r -= 1
            count += 1
        else:
            return -1
    return count

print(solve(p))

