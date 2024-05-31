
def flights_direction(n, sequence):
    return "YES" if sequence.count('SF') > sequence.count('FS') else "NO"

# Input
n = int(input())
sequence = input().strip()

# Output
print(flights_direction(n, sequence))
