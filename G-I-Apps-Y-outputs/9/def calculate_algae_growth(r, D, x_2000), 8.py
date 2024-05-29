
def calculate_algae_growth(r, D, x_2000):
    x_values = [x_2000]
    for i in range(2001, 2011):
        x_i = r * x_values[-1] - D
        x_values.append(x_i)
    
    for x in x_values[1:]:
        print(x)

# Input
r, D, x_2000 = map(int, input().split())

# Calculate and print algae growth
calculate_algae_growth(r, D, x_2000)
```
