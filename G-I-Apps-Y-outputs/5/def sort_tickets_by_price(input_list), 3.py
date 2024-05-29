
def sort_tickets_by_price(input_list):
    n = input_list[0]
    prices = input_list[1:]
    prices.sort()
    return prices

# Reading input
input_list = list(map(int, input().split()))
sorted_prices = sort_tickets_by_price(input_list)
print(*sorted_prices)
```
