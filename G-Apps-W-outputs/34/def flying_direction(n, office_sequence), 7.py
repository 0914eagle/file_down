
def flying_direction(n, office_sequence):
    seattle_to_sf = office_sequence.count('SF')
    sf_to_seattle = office_sequence.count('FS')

    if seattle_to_sf > sf_to_seattle:
        return "YES"
    else:
        return "NO"

# Input
n = int(input())
office_sequence = input().strip()

# Output
print(flying_direction(n, office_sequence))
