
import heapq

def buy_gadgets(n, m, k, s, dollar_rates, pound_rates, gadgets):
    ans = []
    for day in range(1, n+1):
        budget = s
        min_heap = []
        for i, (t, c) in enumerate(gadgets):
            if t == 1:
                cost = c * dollar_rates[day-1]
            else:
                cost = c * pound_rates[day-1]
            
            heapq.heappush(min_heap, (cost, i))
        
        bought = []
        while min_heap and budget >= min_heap[0][0] and len(bought) < k:
            cost, idx = heapq.heappop(min_heap)
            budget -= cost
            bought.append((idx+1, day))
        
        if len(bought) == k:
            ans = [day]
            ans.extend(bought)
            break
    
    if len(ans) == 0:
        return -1
    else:
        return ans

# Input
n, m, k, s = map(int, input().split())
dollar_rates = list(map(int, input().split()))
pound_rates = list(map(int, input().split()))
gadgets = [list(map(int, input().split())) for _ in range(m)]

# Output
result = buy_gadgets(n, m, k, s, dollar_rates, pound_rates, gadgets)
if result == -1:
    print(-1)
else:
    print(result[0])
    for gadget in result[1:]:
        print(gadget[0], gadget[1])
    
```
