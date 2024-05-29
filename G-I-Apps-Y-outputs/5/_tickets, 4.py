_tickets_by_price(arr):
    n = arr[0]
    elements = arr[1:]
    elements.sort()
    return elements

# Input
arr = list(map(int, input().split()))

# Output
sorted_tickets = sort_tickets_by_price(arr)
print(" ".join(map(str, sorted_tickets))
