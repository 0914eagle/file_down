
def catch_criminals(n, a, criminals):
    total_criminals = criminals[a - 1]  # Catch criminal in Limak's city
    
    for distance in range(1, n):
        left_city = a - distance
        right_city = a + distance
        
        if left_city >= 1 and right_city <= n:  # Check if within range
            if criminals[left_city - 1] + criminals[right_city - 1] == 2:
                total_criminals += 2
            else:
                total_criminals += criminals[left_city - 1] + criminals[right_city - 1]
        elif left_city >= 1:  # Check only left
            total_criminals += criminals[left_city - 1]
        elif right_city <= n:  # Check only right
            total_criminals += criminals[right_city - 1]
    
    return total_criminals

# Input parsing
n, a = map(int, input().split())
criminals = list(map(int, input().split()))

# Call the function
print(catch_criminals(n, a, criminals))
```
