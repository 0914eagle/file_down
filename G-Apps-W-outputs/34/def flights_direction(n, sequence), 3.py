
def flights_direction(n, sequence):
    seattle_to_sf = 0
    sf_to_seattle = 0

    for i in range(n - 1):
        if sequence[i] == 'S' and sequence[i + 1] == 'F':
            seattle_to_sf += 1
        elif sequence[i] == 'F' and sequence[i + 1] == 'S':
            sf_to_seattle += 1

    if seattle_to_sf > sf_to_seattle:
        return "YES"
    else:
        return "NO"

# Input processing
n = int(input())
sequence = input().strip()

result = flights_direction(n, sequence)
print(result)
