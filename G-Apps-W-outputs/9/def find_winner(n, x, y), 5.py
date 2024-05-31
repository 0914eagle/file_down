
def find_winner(n, x, y):
    if (x + y) <= (n + 2) and (x + y) % 2 == 0:
        return "White"
    elif (x + y) > (n + 2) or (x + y) % 2 == 1:
        return "Black"

# Read input values
n = int(input())
x, y = map(int, input().split())

# Call the function and print the result
print(find_winner(n, x, y))
