
def calculate_expenses(N, expenses):
    total_expenses = sum(expense for expense in expenses if expense < 0)
    return total_expenses

# Read input
N = int(input())
expenses = list(map(int, input().split()))

# Calculate and print the total expenses
print(calculate_expenses(N, expenses))
