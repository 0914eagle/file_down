
def find_min_day_index(n, m, k, s, dollar_costs, pound_costs, gadgets):
    days_left = n
    gadgets_bought = 0
    budget = s
    day_index = -1
    gadget_purchase_days = {}
    
    for day in range(n):
        dollar_cost = dollar_costs[day]
        pound_cost = pound_costs[day]
        
        for gadget, cost in gadgets:
            if budget >= cost and gadget not in gadget_purchase_days:
                if gadget == 1:
                    converted_cost = cost * dollar_cost
                else:
                    converted_cost = cost * pound_cost
                
                if budget >= converted_cost:
                    budget -= converted_cost
                    gadgets_bought += 1
                    gadget_purchase_days[gadget] = day + 1
                    
                    if gadgets_bought == k:
                        day_index = day + 1
                        break
        
        if gadgets_bought == k:
            break
    
    if gadgets_bought == k:
        print(day_index)
        for gadget in sorted(gadget_purchase_days):
            print(gadget, gadget_purchase_days[gadget])
    else:
        print(-1)

# Input parsing
n, m, k, s = map(int, input().split())
dollar_costs = list(map(int, input().split()))
pound_costs = list(map(int, input().split()))
gadgets = [list(map(int, input().split())) for _ in range(m)]

find_min_day_index(n, m, k, s, dollar_costs, pound_costs, gadgets)
```
