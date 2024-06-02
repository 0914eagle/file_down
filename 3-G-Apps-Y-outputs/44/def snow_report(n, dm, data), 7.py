
def snow_report(n, dm, data):
    for i in range(1, n):
        if data[i] <= dm:
            return f"It hadn't snowed this early in {i-1} years!"
    return "It had never snowed this early!"

# Input parsing
n, dm = map(int, input().split())
data = list(map(int, input().split()))

# Call the function with the input data
result = snow_report(n, dm, data)
print(result)
