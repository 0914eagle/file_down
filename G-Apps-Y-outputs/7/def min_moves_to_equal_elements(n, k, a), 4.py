
def min_moves_to_equal_elements(n, k, a):
    a.sort()
    freq = {}
    for num in a:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    min_val = a[0]
    max_val = a[-1]
    
    moves = 0
    while max_val - min_val > 0 and sum(freq.values()) >= k:
        if freq[min_val] <= freq[max_val]:
            diff = min(k, freq[min_val])
            moves += diff
            k -= diff
            min_val += 1
            if min_val not in freq:
                freq[min_val] = 0
            freq[min_val] += diff
        else:
            diff = min(k, freq[max_val])
            moves += diff
            k -= diff
            max_val -= 1
            if max_val not in freq:
                freq[max_val] = 0
            freq[max_val] += diff
    
    return moves

# Read input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Calculate and print the minimum number of moves required
print(min_moves_to_equal_elements(n, k, a))
