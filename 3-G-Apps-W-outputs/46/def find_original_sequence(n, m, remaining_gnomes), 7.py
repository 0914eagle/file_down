
def find_original_sequence(n, m, remaining_gnomes):
    original_gnomes = [0] * n
    remaining_index = 0
    
    for i in range(n):
        if remaining_index < m and i + 1 == remaining_gnomes[remaining_index]:
            original_gnomes[i] = remaining_gnomes[remaining_index]
            remaining_index += 1

    remaining_index = 0
    for i in range(n):
        if original_gnomes[i] == 0:
            original_gnomes[i] = remaining_gnomes[remaining_index]
            remaining_index += 1

    return original_gnomes

# Read input
n, m = map(int, input().split())
remaining_gnomes = [int(input()) for _ in range(m)]

# Find original sequence
original_sequence = find_original_sequence(n, m, remaining_gnomes)

# Output the original sequence
for gnome in original_sequence:
    print(gnome)
