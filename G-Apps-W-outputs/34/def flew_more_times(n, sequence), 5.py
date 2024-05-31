
def flew_more_times(n, sequence):
    count_SF = 0
    count_FS = 0

    for i in range(n-1):
        if sequence[i] == 'S' and sequence[i+1] == 'F':
            count_SF += 1
        elif sequence[i] == 'F' and sequence[i+1] == 'S':
            count_FS += 1

    if count_SF > count_FS:
        return "YES"
    else:
        return "NO"

# Input
n = int(input())
sequence = input().strip()

# Output
print(flew_more_times(n, sequence))
