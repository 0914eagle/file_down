
def min_coupons(N, trips):
    if N == 0:
        return 0
    
    coupons = 0
    previous_zone = 0
    previous_time = 0
    
    for i in range(N):
        current_zone, current_time = trips[i]
        coupons += 2 + abs(current_zone - previous_zone)
        
        if current_time - previous_time >= 10000:
            previous_zone = current_zone
            previous_time = current_time
        else:
            coupons -= 2
        
    return coupons

# Input parsing
N = int(input())
trips = []
for _ in range(N):
    Z, T = map(int, input().split())
    trips.append((Z, T))

# Calculate and output the minimum number of coupons Johan must purchase
print(min_coupons(N, trips))
```
