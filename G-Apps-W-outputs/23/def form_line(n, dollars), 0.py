
def form_line(n, dollars):
    dollars = [(d, i) for i, d in enumerate(dollars, start=1)]
    dollars.sort(reverse=True)

    for i in range(1, n):
        if dollars[i][0] < dollars[i-1][0]:
            dollars[i] = (dollars[i][0] + 1, dollars[i][1])
        elif dollars[i][0] > dollars[i-1][0]:
            diff = dollars[i][0] - dollars[i-1][0]
            dollars[i] = (dollars[i][0] - diff, dollars[i][1])
            dollars[i-1] = (dollars[i-1][0] + diff, dollars[i-1][1])
    
    dollars.sort(key=lambda x: x[1])
    
    result = [d for d, _ in dollars]
    if all(result[i] >= result[i+1] for i in range(n-1)):
        return result
    else:
        return ":("

# Input reading
n = int(input())
dollars = list(map(int, input().split()))

# Call the function and print the result
result = form_line(n, dollars)
if result == ":(":
    print(result)
else:
    print(*result)
