
def flight_direction(n, sequence):
    seattle_to_sf = sequence.count('SF')
    sf_to_seattle = sequence.count('FS')
    
    if seattle_to_sf > sf_to_seattle:
        return "YES"
    else:
        return "NO"

# Input
n = int(input())
sequence = input().strip()

# Output
print(flight_direction(n, sequence))
