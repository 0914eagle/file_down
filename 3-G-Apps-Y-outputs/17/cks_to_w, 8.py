cks_to_win(H, A):
    if H % A == 0:
        return H // A
    else:
        return H // A + 1

# Read input
H, A = map(int, input().split())

# Calculate and print the number of attacks needed
print(attacks_to_win(H, A))
[/PYTHON