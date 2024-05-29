
def sort_tickets_by_price(arr):
    return sorted(arr)

# Read input
arr = list(map(int, input().split()))

# Sort the array
sorted_arr = sort_tickets_by_price(arr)

# Print the sorted array
for num in sorted_arr:
    print(num, end=' ')
```

