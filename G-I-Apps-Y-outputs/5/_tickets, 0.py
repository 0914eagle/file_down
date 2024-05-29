_tickets_by_price(input_str):
    arr = list(map(int, input_str.split()[1:]))
    arr.sort()
    return ' '.join(map(str, arr))

# Read input from user
input_str = input()
print(sort_tickets_by_price(input_str))
