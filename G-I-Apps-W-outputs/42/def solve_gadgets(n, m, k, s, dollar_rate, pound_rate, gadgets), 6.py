
def solve_gadgets(n, m, k, s, dollar_rate, pound_rate, gadgets):
    cost = [0] * n
    for i in range(n):
        cost[i] = min(s, s // dollar_rate[i]) if i % 2 == 0 else min(s, s // pound_rate[i])
    
    gadget_types = {1: [], 2: []}
    for i, gadget in enumerate(gadgets, start=1):
        gadget_types[gadget[0]].append((gadget[1], i))
    
    gadgets_bought = []
    total_gadgets = 0
    
    for i in range(n):
        gadgets_to_buy = []
        diff = s - cost[i]
        
        if diff < 0:
            break
        
        for cost, gadget_num in gadget_types[1]:
            if cost <= diff and gadget_num not in gadgets_bought:
                gadgets_bought.append(gadget_num)
                gadgets_to_buy.append((gadget_num, i+1))
                total_gadgets += 1
                diff -= cost
                if total_gadgets == k:
                    return (i+1, gadgets_to_buy)
        
        for cost, gadget_num in gadget_types[2]:
            if cost <= diff and gadget_num not in gadgets_bought:
                gadgets_bought.append(gadget_num)
                gadgets_to_buy.append((gadget_num, i+1))
                total_gadgets += 1
                diff -= cost
                if total_gadgets == k:
                    return (i+1, gadgets_to_buy)
    
    return -1

# Input parsing
n, m, k, s = map(int, input().split())
dollar_rate = list(map(int, input().split()))
pound_rate = list(map(int, input().split()))
gadgets = []
for _ in range(m):
    t, c = map(int, input().split())
    gadgets.append((t, c))

min_day, result = solve_gadgets(n, m, k, s, dollar_rate, pound_rate, gadgets)

if min_day == -1:
    print(-1)
else:
    print(min_day)
    for gadget_num, day in result:
        print(gadget_num, day)
