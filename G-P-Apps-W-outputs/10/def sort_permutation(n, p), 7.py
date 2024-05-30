
def sort_permutation(n, p):
    swaps = []
    
    for i in range(n):
        # Find the index of the current element in the sorted permutation
        idx = p.index(i+1)
        
        # If the current element is already in the correct position, continue to the next element
        if idx == i:
            continue
        
        # Calculate the index to swap with
        j = i + 1 if i % 2 == 0 else i - 1
        
        # Perform the swap
        p[i], p[j] = p[j], p[i]
        
        # Record the swap
        swaps.append((i+1, j+1))
    
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

# Read input
n = int(input())
p = list(map(int, input().split()))

# Solve the problem
sort_permutation(n, p)
