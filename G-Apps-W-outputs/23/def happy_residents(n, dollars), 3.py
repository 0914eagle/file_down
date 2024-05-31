
def happy_residents(n, dollars):
    dollars = [0] + dollars
    new_line = [0] * (n + 1)
    
    for i in range(1, n+1):
        if dollars[i] < dollars[i-1]:
            if dollars[i-1] - dollars[i] > 1:
                return ":("
            new_line[i] = dollars[i-1] - 1
            dollars[i-1] = new_line[i]
        else:
            new_line[i] = max(dollars[i], new_line[i-1] + 1)
    
    return new_line[1:] if all(dollars[i] <= new_line[i] for i in range(1, n+1)) else ":("

# Read input
n = int(input())
dollars = list(map(int, input().split()))

# Call the function and print the result
result = happy_residents(n, dollars)
print(' '.join(map(str, result)))
