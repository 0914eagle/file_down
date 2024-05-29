
def calculate_algae_growth(r, D, x_2000):
    result = []
    x_i = x_2000
    for i in range(1, 11):
        x_i = r * x_i - D
        result.append(x_i)
    
    for x in result:
        print(x)

# Input
r, D, x_2000 = map(int, input().split())

# Calculate and output
calculate_algae_growth(r, D, x_2000)
```
