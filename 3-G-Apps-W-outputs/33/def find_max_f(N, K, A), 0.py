
def find_max_f(N, K, A):
    max_f = 0
    for i in range(40, -1, -1):
        count_one = 0
        mask = 1 << i
        new_max_f = max_f | (1 << i)
        
        for a in A:
            if a & mask:
                count_one += 1
        
        if count_one <= N // 2 and new_max_f <= K:
            max_f = new_max_f
    
    return sum(new_max_f ^ a for a in A)

# Read input
N, K = map(int, input().split())
A = list(map(int, input().split()))

# Find and print the maximum value of f
print(find_max_f(N, K, A))
