
def find_min_max_players(a1, a2, k1, k2, n):
    # Calculate the maximum number of players that could have been sent off
    max_players_left = min(a1, n // k1) + min(a2, (n - min(a1, n // k1) * k1) // k2)
    
    # Calculate the minimum number of players that could have been sent off
    min_players_left = max(0, n - (a1 * (k1 - 1) + a2 * (k2 - 1)))
    
    print(min_players_left, max_players_left)

# Read inputs from the user
a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())

# Call the function with the inputs
find_min_max_players(a1, a2, k1, k2, n)
