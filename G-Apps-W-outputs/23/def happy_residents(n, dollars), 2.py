
def happy_residents(n, dollars):
    line = [0] * n
    for i in range(n):
        line[i] = i + 1
    
    dollars.sort(reverse=True)
    for i in range(n):
        if dollars[line[i]-1] < dollars[i]:
            return ":("
    
    for i in range(n):
        line[i] = dollars[i]
    
    return " ".join(map(str, line))


# Input
n = 3
dollars = [12, 3, 3]

# Output
print(happy_residents(n, dollars))
