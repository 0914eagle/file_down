
import heapq

def solve(n, m, k, s, a, b, gadgets):
    days_gadgets = [[] for _ in range(n)]
    dollars_heap = []
    pounds_heap = []
    
    for i in range(m):
        t, c = gadgets[i]
        if t == 1:
            heapq.heappush(dollars_heap, (c, i+1))
        else:
            heapq.heappush(pounds_heap, (c, i+1))
    
    for i in range(n):
        while dollars_heap and dollars_heap[0][1] < i+1:
            heapq.heappop(dollars_heap)
        while pounds_heap and pounds_heap[0][1] < i+1:
            heapq.heappop(pounds_heap)
        
        for j in range(len(dollars_heap)+1):
            day = i + j
            remaining_gadgets = k - len(days_gadgets[day])
            
            if day >= n or remaining_gadgets <= 0:
                break
            
            dollars_cost = dollars_heap[j][0] * a[i]
            pounds_cost = pounds_heap[min(len(pounds_heap)-1, remaining_gadgets-1)][0] * b[i]
            
            if dollars_cost <= s and dollars_cost <= pounds_cost:
                for gadget_index in range(j+1):
                    gadget = dollars_heap[gadget_index][1]
                    days_gadgets[day].append((gadget, i+1))
                s -= dollars_cost
            elif pounds_cost <= s:
                for gadget_index in range(remaining_gadgets):
                    gadget = pounds_heap[gadget_index][1]
                    days_gadgets[day].append((gadget, i+1))
                s -= pounds_cost

    for day, gadgets in enumerate(days_gadgets):
        if len(gadgets) == k:
            return day+1, gadgets
    
    return -1

# Input parsing
n, m, k, s = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
gadgets = [list(map(int, input().split())) for _ in range(m)]

# Call the solve function
result = solve(n, m, k, s, a, b, gadgets)

# Output formatting
if result == -1:
    print(-1)
else:
    day, gadgets = result
    print(day)
    for gadget in gadgets:
        print(gadget[0], gadget[1])
