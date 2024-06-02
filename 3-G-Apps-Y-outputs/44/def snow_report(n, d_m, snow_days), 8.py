
def snow_report(n, d_m, snow_days):
    k = 0
    for i in range(1, n):
        if snow_days[i] > d_m:
            k += 1
        else:
            break
    
    if k > 0:
        print(f"It hadn't snowed this early in {k} years!")
    else:
        print("It had never snowed this early!")

# Read input
n, d_m = map(int, input().split())
snow_days = list(map(int, input().split()))

# Call the function with the input values
snow_report(n, d_m, snow_days)
