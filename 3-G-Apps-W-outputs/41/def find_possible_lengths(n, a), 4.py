
def find_possible_lengths(n, a):
    possible_lengths = []
    
    for k in range(1, n+1):
        x = [a[i] - a[i-1] for i in range(1, n+1) if (i-1) % k < len(a)]
        valid = True
        
        for i in range(1, n):
            if a[i] != x[(i-1) % len(x)] + a[i-1]:
                valid = False
                break
        
        if valid:
            possible_lengths.append(k)
    
    return len(possible_lengths), possible_lengths

# Input
n = int(input())
a = list(map(int, input().split()))

# Output
l, possible_lengths = find_possible_lengths(n, a)
print(l)
print(*possible_lengths)
