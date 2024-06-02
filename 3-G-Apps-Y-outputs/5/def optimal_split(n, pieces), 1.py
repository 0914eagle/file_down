
def optimal_split(n, pieces):
    pieces.sort(reverse=True)  # Sort the pieces in descending order
    
    alice_sum = 0
    bob_sum = 0
    
    for i in range(n):
        if i % 2 == 0:  # Alice's turn
            alice_sum += pieces[i]
        else:  # Bob's turn
            bob_sum += pieces[i]
    
    return alice_sum, bob_sum

# Read input
n = int(input())
pieces = list(map(int, input().split()))

# Call the function and print the output
alice_sum, bob_sum = optimal_split(n, pieces)
print(alice_sum, bob_sum)
