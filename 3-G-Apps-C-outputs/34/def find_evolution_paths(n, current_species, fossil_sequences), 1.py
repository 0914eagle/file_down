
def find_evolution_paths(n, current_species, fossil_sequences):
    path1 = []
    path2 = []
    
    for sequence in fossil_sequences:
        if all(nuc in current_species for nuc in sequence):
            path1.append(sequence)
        elif all(nuc not in current_species for nuc in sequence):
            path2.append(sequence)
        else:
            return "impossible"
    
    return f"{len(path1)} {len(path2)}\n" + "\n".join(path1) + "\n" + "\n".join(path2)

# Sample Input
n = 5
current_species = "AACCMMAA"
fossil_sequences = ["ACA", "MM", "ACMAA", "AA", "A"]

print(find_evolution_paths(n, current_species, fossil_sequences))
