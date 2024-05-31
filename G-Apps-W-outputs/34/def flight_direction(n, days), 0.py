
def flight_direction(n, days):
    count_SF_to_Seattle = 0
    count_Seattle_to_SF = 0
    
    for i in range(n-1):
        if days[i] == 'S' and days[i+1] == 'F':
            count_Seattle_to_SF += 1
        elif days[i] == 'F' and days[i+1] == 'S':
            count_SF_to_Seattle += 1
    
    return "YES" if count_Seattle_to_SF > count_SF_to_Seattle else "NO"

# Input
n = int(input())
days = input().strip()

# Output
print(flight_direction(n, days))
