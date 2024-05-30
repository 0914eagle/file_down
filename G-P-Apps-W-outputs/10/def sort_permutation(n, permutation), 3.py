
def sort_permutation(n, permutation):
    swaps = []
    
    def swap(i, j):
        swaps.append((i+1, j+1))  # Adjust indices to be 1-based
        permutation[i], permutation[j] = permutation[j], permutation[i]
    
    for i in range(n):
        while i != permutation[i]-1:
            j = permutation[i]-1
            if 2 * abs(i - j) >= n:
                swap(i, j)
            else:
                for k in range(i+1, n):
                    if 2 * abs(k - j) >= n:
                        swap(k, j)
                        swap(i, j)
                        break
    
    print(len(swaps))
    for a, b in swaps:
        print(a, b)

# Input reading
n = int(input())
permutation = list(map(int, input().split()))

sort_permutation(n, permutation)
