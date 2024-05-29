_tickets_by_price(array):
    array.sort()
    return ' '.join(map(str, array))

# Input
input_array = input().split()
n = int(input_array[0])
tickets_prices = list(map(int, input_array[1:]))

# Sort the array
sorted_prices = sort_tickets_by_price(tickets_prices)

# Output
print(sorted_prices)
