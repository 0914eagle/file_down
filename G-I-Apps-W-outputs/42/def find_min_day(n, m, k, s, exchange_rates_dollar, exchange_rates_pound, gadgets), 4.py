
def find_min_day(n, m, k, s, exchange_rates_dollar, exchange_rates_pound, gadgets):
    sufficient_gadgets = []
    
    for day in range(n):
        budget = s
        gadgets_bought = []
        
        for gadget_id, (gadget_type, cost) in enumerate(gadgets):
            if gadget_id in sufficient_gadgets:
                continue

            cost_in_burles = cost
            if gadget_type == 1:  # Dollar
                cost_in_burles *= exchange_rates_dollar[day]
            else:  # Pound
                cost_in_burles *= exchange_rates_pound[day]

            if budget >= cost_in_burles:
                budget -= cost_in_burles
                gadgets_bought.append((gadget_id + 1, day + 1))

            if len(gadgets_bought) == k:
                return day + 1, gadgets_bought
        
        if len(gadgets_bought) == k:
            return day + 1, gadgets_bought
    
    return -1

# Input parsing
n, m, k, s = map(int, input().split())
exchange_rates_dollar = list(map(int, input().split()))
exchange_rates_pound = list(map(int, input().split()))

gadgets = []
for _ in range(m):
    t, c = map(int, input().split())
    gadgets.append((t, c))

# Call the function and print the result
min_day, bought_gadgets = find_min_day(n, m, k, s, exchange_rates_dollar, exchange_rates_pound, gadgets)
if min_day == -1:
    print(-1)
else:
    print(min_day)
    for gadget_id, day_bought in bought_gadgets:
        print(gadget_id, day_bought)
```
