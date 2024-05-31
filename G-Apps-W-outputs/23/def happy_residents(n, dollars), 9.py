
def happy_residents(n, dollars):
    new_line = [0] * n
    for i in range(n):
        new_line[i] = i + 1
    
    dollars.sort()
    for i in range(n):
        if dollars[i] < new_line[i] - i:
            return ":("
    
    for i in range(n):
        new_line[i] = dollars[i]
    
    return " ".join(map(str, new_line))

# Input
n = int(input())
dollars = list(map(int, input().split()))

# Output
print(happy_residents(n, dollars))
