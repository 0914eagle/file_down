
def calculate_expenses(N, expenses):
    total_expenses = 0
    for expense in expenses:
        if expense < 0:
            total_expenses += expense
    return total_expenses

# Input
N = int(input())
expenses = list(map(int, input().split()))

# Calculate and output expenses
result = calculate_expenses(N, expenses)
print(result)
