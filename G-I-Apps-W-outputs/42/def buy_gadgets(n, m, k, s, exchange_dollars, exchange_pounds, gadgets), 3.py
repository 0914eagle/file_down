
def buy_gadgets(n, m, k, s, exchange_dollars, exchange_pounds, gadgets):
    min_day = -1
    for day in range(n):
        remaining_burles = s
        bought_gadgets = []
        for i in range(m):
            gadget_type, cost = gadgets[i]
            if gadget_type == 1:
                cost_burles = cost * exchange_dollars[day]
            else:
                cost_burles = cost * exchange_pounds[day]
            
            if cost_burles <= remaining_burles:
                remaining_burles -= cost_burles
                bought_gadgets.append((i+1, day+1))
            
            if len(bought_gadgets) == k:
                min_day = day
                break
        
        if len(bought_gadgets) == k:
            break
    
    if min_day == -1:
        print(-1)
    else:
        print(min_day+1)
        for gadget in bought_gadgets:
            print(gadget[0], gadget[1])

# Input parsing
n, m, k, s = map(int, input().split())
exchange_dollars = list(map(int, input().split()))
exchange_pounds = list(map(int, input().split()))
gadgets = []
for _ in range(m):
    t, c = map(int, input().split())
    gadgets.append((t, c))

buy_gadgets(n, m, k, s, exchange_dollars, exchange_pounds, gadgets)
```
