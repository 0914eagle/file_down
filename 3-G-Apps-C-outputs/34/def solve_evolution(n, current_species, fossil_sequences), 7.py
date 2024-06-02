
def solve_evolution(n, current_species, fossil_sequences):
    path1 = []
    path2 = []
    
    for sequence in fossil_sequences:
        if set(sequence) == set(current_species):
            return "impossible"
        
        if set(sequence) & set(current_species):
            if len(path1) == 0:
                path1.append(sequence)
            elif len(path2) == 0:
                path2.append(sequence)
            else:
                return "impossible"
        else:
            path1.append(sequence)
    
    return f"{len(path1)} {len(path2)}\n" + "\n".join(path1) + "\n" + "\n".join(path2)

# Input
n = int(input())
current_species = input().strip()
fossil_sequences = [input().strip() for _ in range(n)]

# Output
print(solve_evolution(n, current_species, fossil_sequences))
