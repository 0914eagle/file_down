
def validate_evolution(n, current_species, fossil_sequences):
    path1 = []
    path2 = []
    
    for sequence in fossil_sequences:
        if set(sequence) == set(current_species):
            path1.append(sequence)
        elif all(nucleotide in current_species for nucleotide in sequence):
            path2.append(sequence)
        else:
            return "impossible"
    
    return f"{len(path1)} {len(path2)}\n" + "\n".join(path1) + "\n" + "\n".join(path2)

# Sample Input 1
n = 5
current_species = "AACCMMAA"
fossil_sequences = ["ACA", "MM", "ACMAA", "AA", "A"]
print(validate_evolution(n, current_species, fossil_sequences))

# Sample Input 2
n = 3
current_species = "ACMA"
fossil_sequences = ["ACM", "ACA", "AMA"]
print(validate_evolution(n, current_species, fossil_sequences))

# Sample Input 3
n = 1
current_species = "AM"
fossil_sequences = ["MA"]
print(validate_evolution(n, current_species, fossil_sequences))
