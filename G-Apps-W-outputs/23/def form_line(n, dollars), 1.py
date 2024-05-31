
def form_line(n, dollars):
    dollars.sort()
    result = [0] * n
    for i in range(n):
        if i > 0 and dollars[i] == dollars[i-1]:
            result[i] = result[i-1]
        else:
            result[i] = dollars[i]
    
    for i in range(n-1):
        if result[i] > result[i+1]:
            return ":("
    
    return ' '.join(map(str, result))

# Read input
n = int(input())
dollars = list(map(int, input().split()))

# Call the function and print the result
print(form_line(n, dollars))
