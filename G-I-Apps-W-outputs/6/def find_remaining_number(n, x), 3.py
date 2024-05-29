
def find_remaining_number(n, x):
    if x == 1:
        return 1
    remaining_numbers = n - x
    return 2 * remaining_numbers

# Read the number of queries
T = int(input())

for _ in range(T):
    n, x = map(int, input().split())
    print(find_remaining_number(n, x))
    
