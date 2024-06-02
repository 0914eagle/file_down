
def find_original_sequence(n, m, remaining_gnomes):
    original_sequence = []
    used = [False] * (n + 1)
    
    for gnome in remaining_gnomes:
        used[gnome] = True
    
    current = 1
    for gnome in remaining_gnomes:
        while current < gnome:
            if not used[current]:
                original_sequence.append(current)
                used[current] = True
            current += 1
        original_sequence.append(gnome)
    
    for i in range(1, n + 1):
        if not used[i]:
            original_sequence.append(i)
    
    return original_sequence

# Read input
n, m = map(int, input().split())
remaining_gnomes = [int(input()) for _ in range(m)]

# Find the original sequence
original_sequence = find_original_sequence(n, m, remaining_gnomes)

# Output the original sequence
for gnome in original_sequence:
    print(gnome)
