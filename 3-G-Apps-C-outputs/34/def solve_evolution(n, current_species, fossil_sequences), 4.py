
def solve_evolution(n, current_species, fossil_sequences):
    path1 = []
    path2 = []
    
    for sequence in fossil_sequences:
        if set(sequence) == set(current_species):
            return "impossible"
        
        if set(sequence) & set(current_species):
            if set(sequence) in [set(x) for x in path1]:
                path1.append(sequence)
            elif set(sequence) in [set(x) for x in path2]:
                path2.append(sequence)
            else:
                return "impossible"
        else:
            if not path1:
                path1.append(sequence)
            else:
                path2.append(sequence)
    
    return f"{len(path1)} {len(path2)}\n" + "\n".join(path1) + "\n" + "\n".join(path2)

# Input
n = 5
current_species = "AACCMMAA"
fossil_sequences = ["ACA", "MM", "ACMAA", "AA", "A"]

# Output
print(solve_evolution(n, current_species, fossil_sequences))
