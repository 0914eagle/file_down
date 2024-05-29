
def solve_gadgets(n, m, k, s, dollar_rates, pound_rates, gadgets):
    min_day = -1
    min_cost = float('inf')
    
    for day in range(1, n+1):
        remaining_burles = s
        bought_gadgets = []
        
        for i in range(m):
            gadget_type, cost = gadgets[i]
            
            if gadget_type == 1:
                gadget_cost = cost * dollar_rates[day-1]
            else:
                gadget_cost = cost * pound_rates[day-1]
            
            if gadget_cost <= remaining_burles and len(bought_gadgets) < k:
                bought_gadgets.append((i+1, day))
                remaining_burles -= gadget_cost
        
        if len(bought_gadgets) == k and day < min_cost:
            min_day = day
            min_cost = day

    if min_day == -1:
        print(-1)
    else:
        print(min_day)
        for gadget in bought_gadgets:
            print(gadget[0], gadget[1])

# Input
n, m, k, s = map(int, input().split())
dollar_rates = list(map(int, input().split()))
pound_rates = list(map(int, input().split()))
gadgets = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function
solve_gadgets(n, m, k, s, dollar_rates, pound_rates, gadgets)
```
