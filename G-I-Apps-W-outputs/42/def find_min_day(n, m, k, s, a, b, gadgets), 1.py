
def find_min_day(n, m, k, s, a, b, gadgets):
    min_day_index = -1
    possible_days = []
    
    for day in range(1, n+1):
        cost_per_gadget = []
        for i in range(m):
            t, c = gadgets[i]
            if t == 1:  # cost is in dollars
                cost_per_gadget.append((c, a[day-1]))
            else:  # cost is in pounds
                cost_per_gadget.append((c, b[day-1]))
        
        cost_per_gadget.sort()
        
        total_cost = 0
        bought_gadgets = set()
        
        for cost, currency_rate in cost_per_gadget:
            if total_cost + cost <= s and len(bought_gadgets) < k:
                total_cost += cost
                bought_gadgets.add(cost)
                if len(bought_gadgets) == k:
                    min_day_index = day
                    possible_days = list(bought_gadgets)
    
    if min_day_index == -1:
        print(min_day_index)
    else:
        print(min_day_index)
        for gadget in possible_days:
            for i in range(m):
                if gadgets[i][1] == gadget:
                    print(i+1, min_day_index)

# Input parsing
n, m, k, s = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

gadgets = []
for _ in range(m):
    t, c = map(int, input().split())
    gadgets.append((t, c))

find_min_day(n, m, k, s, a, b, gadgets)
```
