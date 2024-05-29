
def sort_tickets_by_price(arr):
    return sorted(arr)

# Read input
input_arr = list(map(int, input().split()))
n, tickets = input_arr[0], input_arr[1:]

# Sort and print the array
sorted_tickets = sort_tickets_by_price(tickets)
print(*sorted_tickets)
```
