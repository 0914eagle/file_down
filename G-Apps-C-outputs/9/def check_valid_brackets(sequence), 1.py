
def check_valid_brackets(sequence):
    n = len(sequence)
    balance = 0
    for char in sequence:
        if char == '(':
            balance += 1
        else:
            balance -= 1
            if balance < -1:
                return "impossible"

    if balance == 0:
        return "possible"

    if balance == 2:
        return "possible" if sequence[0] == '(' or sequence[n-1] == ')' else "impossible"

    if balance == -2:
        return "possible" if sequence[0] == ')' or sequence[n-1] == '(' else "impossible"

    return "impossible"

# Input
bracket_sequence = input().strip()

# Check if it is possible to make the sequence valid
result = check_valid_brackets(bracket_sequence)
print(result)
