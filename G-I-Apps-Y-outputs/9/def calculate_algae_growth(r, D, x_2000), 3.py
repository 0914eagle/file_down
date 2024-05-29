
def calculate_algae_growth(r, D, x_2000):
    x_values = []
    x_values.append(x_2000)
    
    for i in range(2001, 2011):
        x_next = r * x_values[-1] - D
        x_values.append(x_next)
    
    for x_value in x_values[1:]:
        print(x_value)

# Sample Input
r, D, x_2000 = map(int, input().split())
calculate_algae_growth(r, D, x_2000)
```
