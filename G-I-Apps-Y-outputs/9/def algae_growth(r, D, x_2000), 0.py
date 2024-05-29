
def algae_growth(r, D, x_2000):
    x_values = []
    x_values.append(x_2000)
    
    for i in range(10):
        x_next = r * x_values[-1] - D
        x_values.append(x_next)
    
    for i in range(1, 11):
        print(x_values[i])

# Get input values
r, D, x_2000 = map(int, input().split())
algae_growth(r, D, x_2000)
```
