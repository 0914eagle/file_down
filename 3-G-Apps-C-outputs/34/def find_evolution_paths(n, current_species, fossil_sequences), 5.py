
def find_evolution_paths(n, current_species, fossil_sequences):
    first_path = []
    second_path = []
    
    for sequence in fossil_sequences:
        if set(sequence) == set(current_species):
            first_path.append(sequence)
        elif all(nucleotide in current_species for nucleotide in sequence):
            second_path.append(sequence)
        else:
            return "impossible"
    
    return f"{len(first_path)} {len(second_path)}\n" + "\n".join(first_path) + "\n" + "\n".join(second_path)

# Sample Input 1
n = 5
current_species = "AACCMMAA"
fossil_sequences = ["ACA", "MM", "ACMAA", "AA", "A"]
print(find_evolution_paths(n, current_species, fossil_sequences))

# Sample Input 2
n = 3
current_species = "ACMA"
fossil_sequences = ["ACM", "ACA", "AMA"]
print(find_evolution_paths(n, current_species, fossil_sequences))

# Sample Input 3
n = 1
current_species = "AM"
fossil_sequences = ["MA"]
print(find_evolution_paths(n, current_species, fossil_sequences))
