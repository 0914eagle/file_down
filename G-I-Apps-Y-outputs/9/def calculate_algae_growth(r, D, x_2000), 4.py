
def calculate_algae_growth(r, D, x_2000):
    x = x_2000
    for i in range(1, 11):
        x = r * x - D
        print(int(x))

# Input
r, D, x_2000 = map(int, input().split())

# Calculate and print algae growth
calculate_algae_growth(r, D, x_2000)
```
