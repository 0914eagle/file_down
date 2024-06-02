
def find_evolution_paths(n, current_species, fossil_sequences):
    path1 = []
    path2 = []
    
    for sequence in fossil_sequences:
        if sequence == current_species:
            continue
        
        if all(nucleotide in current_species for nucleotide in sequence):
            path1.append(sequence)
        elif all(nucleotide in sequence for nucleotide in current_species):
            path2.append(sequence)
        else:
            return "impossible"
    
    return f"{len(path1)} {len(path2)}\n" + "\n".join(path1) + "\n" + "\n".join(path2)

# Sample Input 1
n1 = 5
current_species1 = "AACCMMAA"
fossil_sequences1 = ["ACA", "MM", "ACMAA", "AA", "A"]
print(find_evolution_paths(n1, current_species1, fossil_sequences1))

# Sample Input 2
n2 = 3
current_species2 = "ACMA"
fossil_sequences2 = ["ACM", "ACA", "AMA"]
print(find_evolution_paths(n2, current_species2, fossil_sequences2))

# Sample Input 3
n3 = 1
current_species3 = "AM"
fossil_sequences3 = ["MA"]
print(find_evolution_paths(n3, current_species3, fossil_sequences3))
