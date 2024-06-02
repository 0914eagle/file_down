cks_needed_to_win(H, A):
    if H % A == 0:
        return H // A
    else:
        return H // A + 1

# Read input from Standard Input
H, A = map(int, input().split())

# Calculate and print the number of attacks needed to win
print(attacks_needed_to_win(H, A))
[/PYTHON