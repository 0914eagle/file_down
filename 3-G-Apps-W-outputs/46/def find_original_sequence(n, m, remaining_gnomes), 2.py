
def find_original_sequence(n, m, remaining_gnomes):
    original_gnomes = []
    remaining_index = 0
    for i in range(1, n + 1):
        if remaining_index < m and i == remaining_gnomes[remaining_index]:
            remaining_index += 1
        else:
            original_gnomes.append(i)
    
    return original_gnomes

# Read input
n, m = map(int, input().split())
remaining_gnomes = [int(input()) for _ in range(m)]

# Find and output the original sequence
original_sequence = find_original_sequence(n, m, remaining_gnomes)
for gnome in original_sequence:
    print(gnome)
