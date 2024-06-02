
def consecutive_years(n, dm, data):
    k = 0
    for i in range(1, n):
        if data[i] > dm:
            k += 1
        else:
            break
    
    if k > 0:
        print(f"It hadn't snowed this early in {k} years!")
    else:
        print("It had never snowed this early!")

# Read input
n, dm = map(int, input().split())
data = list(map(int, input().split()))

# Call the function
consecutive_years(n, dm, data)
