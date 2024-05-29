
from collections import deque

def minimize_coupons(N, trips):
    tickets = deque()
    coupons = 0
    
    for trip in trips:
        Z, T = trip
        
        while tickets and tickets[0][1] <= T:
            tickets.popleft()
        
        if not tickets or Z < tickets[0][0] or Z > tickets[-1][1]:
            A = Z
            B = Z
            while tickets and tickets[0][0] < A:
                A = tickets[0][0]
            while tickets and tickets[-1][1] > B:
                B = tickets[-1][1]
            
            new_tickets = (A, B)
            coupons += 2 + abs(A - B)
            tickets.append(new_tickets)
    
    return coupons

# Input
N = 3
trips = [(1, 4), (2, 10), (0, 15)]

# Output
print(minimize_coupons(N, trips))
```
