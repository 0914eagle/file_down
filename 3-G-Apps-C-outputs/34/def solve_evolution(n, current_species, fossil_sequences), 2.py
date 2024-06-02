
def solve_evolution(n, current_species, fossil_sequences):
    first_path = []
    second_path = []
    
    for sequence in fossil_sequences:
        if set(sequence) == set(current_species):
            second_path.append(sequence)
        else:
            first_path.append(sequence)
    
    if len(first_path) == 0 or len(second_path) == 0:
        print("impossible")
    else:
        print(len(first_path), len(second_path))
        for seq in first_path:
            print(seq)
        for seq in second_path:
            print(seq)

# Sample Input 1
n = 5
current_species = "AACCMMAA"
fossil_sequences = ["ACA", "MM", "ACMAA", "AA", "A"]
solve_evolution(n, current_species, fossil_sequences)

# Sample Input 2
n = 3
current_species = "ACMA"
fossil_sequences = ["ACM", "ACA", "AMA"]
solve_evolution(n, current_species, fossil_sequences)

# Sample Input 3
n = 1
current_species = "AM"
fossil_sequences = ["MA"]
solve_evolution(n, current_species, fossil_sequences)
