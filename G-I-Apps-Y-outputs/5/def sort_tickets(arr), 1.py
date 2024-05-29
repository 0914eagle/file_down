
def sort_tickets(arr):
    arr.sort()
    return arr

# Get input
n, *arr = map(int, input().split())

# Call the function and print the output
sorted_arr = sort_tickets(arr)
print(*sorted_arr)
```
