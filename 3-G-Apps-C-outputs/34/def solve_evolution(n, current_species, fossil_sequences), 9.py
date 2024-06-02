
def solve_evolution(n, current_species, fossil_sequences):
    path1 = []
    path2 = []
    
    for sequence in fossil_sequences:
        if sequence == current_species:
            continue
        
        valid_path1 = True
        valid_path2 = True
        
        for i in range(len(sequence)):
            if sequence[i] != current_species[i]:
                if current_species[i] not in ['A', 'C', 'M']:
                    valid_path1 = False
                if sequence[i] not in ['A', 'C', 'M']:
                    valid_path2 = False
        
        if valid_path1:
            path1.append(sequence)
        elif valid_path2:
            path2.append(sequence)
        else:
            return "impossible"
    
    return f"{len(path1)} {len(path2)}\n" + "\n".join(path1) + "\n" + "\n".join(path2)

# Input
n = int(input())
current_species = input().strip()
fossil_sequences = [input().strip() for _ in range(n)]

# Output
print(solve_evolution(n, current_species, fossil_sequences))
