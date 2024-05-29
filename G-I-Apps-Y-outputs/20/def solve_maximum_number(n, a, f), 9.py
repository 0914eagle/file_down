
def solve_maximum_number(n, a, f):
    a = list(map(int, a))
    f = [0] + f  # to match 1-indexed f function
    used = set()
    
    max_num = a[:]
    for i in range(n):
        if f[a[i]] > a[i] and a[i] not in used:
            max_num[i] = f[a[i]]
            used.add(a[i])
        else:
            break
    
    return ''.join(map(str, max_num))

# Input
n = int(input())
a = input().strip()
f = list(map(int, input().split()))

# Output
result = solve_maximum_number(n, a, f)
print(result)
