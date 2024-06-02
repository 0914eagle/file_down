
def find_possible_lengths(n, a):
    possible_lengths = []
    
    for k in range(1, n+1):
        x = []
        for i in range(1, n+1):
            x_i = a[i] - a[i-1]
            if x_i < 0:
                break
            if x_i != a[(i-1) % k]:
                break
            x.append(x_i)
        if len(x) == n:
            possible_lengths.append(k)
    
    return len(possible_lengths), possible_lengths

# Input
n = int(input())
a = list(map(int, input().split()))

# Output
l, possible_lengths = find_possible_lengths(n, a)
print(l)
print(*possible_lengths)
