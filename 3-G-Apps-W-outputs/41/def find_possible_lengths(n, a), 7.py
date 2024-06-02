
def find_possible_lengths(n, a):
    possible_lengths = []
    
    for k in range(1, n+1):
        x = [a[i] - a[i-1] for i in range(1, n+1)]
        valid = True
        
        for i in range(n):
            if x[i % k] + a[i] != a[i+1]:
                valid = False
                break
        
        if valid:
            possible_lengths.append(k)
    
    return len(possible_lengths), possible_lengths

# Input
n = int(input())
a = list(map(int, input().split()))

# Output
l, lengths = find_possible_lengths(n, a)
print(l)
print(" ".join(map(str, lengths)))
