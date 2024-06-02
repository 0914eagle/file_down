
def snow_analysis(n, d_m, snow_data):
    for i in range(1, n+1):
        if snow_data[-i] <= d_m:
            if i == 1:
                return f"It hadn't snowed this early in {i-1} year!"
            else:
                return f"It hadn't snowed this early in {i-1} years!"
    
    return "It had never snowed this early!"

# Sample Input 1
n1, d_m1 = 4, 2
snow_data1 = [3, 3, 3, 2]
print(snow_analysis(n1, d_m1, snow_data1))

# Sample Input 2
n2, d_m2 = 2, 10
snow_data2 = [0, 100]
print(snow_analysis(n2, d_m2, snow_data2))
