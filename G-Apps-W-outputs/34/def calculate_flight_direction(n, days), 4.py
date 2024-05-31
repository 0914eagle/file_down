
def calculate_flight_direction(n, days):
    seattle_to_sf = 0
    sf_to_seattle = 0
    
    for i in range(n - 1):
        if days[i] == 'S' and days[i + 1] == 'F':
            seattle_to_sf += 1
        elif days[i] == 'F' and days[i + 1] == 'S':
            sf_to_seattle += 1
    
    if seattle_to_sf > sf_to_seattle:
        return "YES"
    else:
        return "NO"

# Input parsing
n = int(input())
days = input().strip()

# Calculate and print the result
print(calculate_flight_direction(n, days))
