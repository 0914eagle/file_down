
def snow_analysis(n, d_m, snow_data):
    k = 0
    for i in range(1, n):
        if snow_data[i] > d_m:
            k += 1
        else:
            break
    
    if k > 0:
        print(f"It hadn't snowed this early in {k} years!")
    else:
        print("It had never snowed this early!")

# Input processing
n, d_m = map(int, input().split())
snow_data = list(map(int, input().split()))

snow_analysis(n, d_m, snow_data)
