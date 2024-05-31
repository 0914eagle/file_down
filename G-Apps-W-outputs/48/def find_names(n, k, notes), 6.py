
def find_names(n, k, notes):
    names = []
    for i in range(n):
        if i < k-1:
            names.append('A') # Start with the first letter being 'A'
        else:
            if notes[i-k+1] == 'YES':
                names.append(chr(ord('A') + i % k)) # Use consecutive letters for effective groups
            else:
                names.append('A') # If group is not effective, use 'A' for the name
    return names

# Input
n, k = map(int, input().split())
notes = input().split()

# Output
result = find_names(n, k, notes)
print(" ".join(result))
