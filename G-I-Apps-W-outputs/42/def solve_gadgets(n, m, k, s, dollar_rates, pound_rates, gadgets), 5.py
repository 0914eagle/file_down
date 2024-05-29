
def solve_gadgets(n, m, k, s, dollar_rates, pound_rates, gadgets):
    possible_solutions = []
    
    for day in range(n):
        remaining_burles = s
        used_gadgets = set()
        bought_gadgets = []
        
        for i in range(m):
            t, c = gadgets[i]
            gadget_cost = c
            
            if t == 1:  # Gadget cost in dollars
                exchange_rate = dollar_rates[day]
                gadget_cost *= exchange_rate
            else:  # Gadget cost in pounds
                exchange_rate = pound_rates[day]
                gadget_cost *= exchange_rate
            
            if gadget_cost <= remaining_burles:
                remaining_burles -= gadget_cost
                used_gadgets.add(i + 1)
                bought_gadgets.append([i + 1, day + 1])
                
                if len(used_gadgets) == k:
                    return day + 1, bought_gadgets
                
        if len(used_gadgets) == k:
            possible_solutions.append((day + 1, bought_gadgets))
    
    if possible_solutions:
        day, bought_gadgets = possible_solutions[0]
        print(day)
        for gadget in bought_gadgets:
            print(gadget[0], gadget[1])
    else:
        print(-1)


# Input parsing
n, m, k, s = map(int, input().split())
dollar_rates = list(map(int, input().split()))
pound_rates = list(map(int, input().split()))
gadgets = [list(map(int, input().split())) for _ in range(m)]

solve_gadgets(n, m, k, s, dollar_rates, pound_rates, gadgets)
```
