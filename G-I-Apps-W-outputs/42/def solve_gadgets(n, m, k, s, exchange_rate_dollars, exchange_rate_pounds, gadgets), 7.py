
def solve_gadgets(n, m, k, s, exchange_rate_dollars, exchange_rate_pounds, gadgets):
    remaining_days = n
    remaining_gadgets = k
    remaining_burles = s
    bought_gadgets = {}
    
    # Sort gadgets by cost and type
    gadgets.sort(key=lambda x: (x[1], x[0]))
    
    day_index = 1
    while day_index <= n and remaining_days > 0 and remaining_gadgets > 0:
        cost_dollars = exchange_rate_dollars[day_index - 1]
        cost_pounds = exchange_rate_pounds[day_index - 1]
        
        for i, gadget in enumerate(gadgets):
            gadget_type, cost = gadget
            if gadget_type == 1 and cost * cost_dollars <= remaining_burles:
                remaining_burles -= cost * cost_dollars
                bought_gadgets[i + 1] = day_index
                remaining_gadgets -= 1
            elif gadget_type == 2 and cost * cost_pounds <= remaining_burles:
                remaining_burles -= cost * cost_pounds
                bought_gadgets[i + 1] = day_index
                remaining_gadgets -= 1
                
        remaining_days -= 1
        day_index += 1
        
    if remaining_gadgets > 0:
        return -1
    else:
        return bought_gadgets

# Input parsing
n, m, k, s = map(int, input().split())
exchange_rate_dollars = list(map(int, input().split()))
exchange_rate_pounds = list(map(int, input().split()))

gadgets = []
for _ in range(m):
    t, c = map(int, input().split())
    gadgets.append((t, c))

# Call the function and print the output
result = solve_gadgets(n, m, k, s, exchange_rate_dollars, exchange_rate_pounds, gadgets)

if result == -1:
    print(-1)
else:
    print(len(result))
    for gadget, day in result.items():
        print(gadget, day)
```
