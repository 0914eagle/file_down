
def calculate_algae_growth(r, D, x_2000):
    x_values = []
    x_values.append(r * x_2000 - D)
    for _ in range(9):
        x_values.append(r * x_values[-1] - D)

    for x in x_values:
        print(x)

r, D, x_2000 = map(int, input().split())
calculate_algae_growth(r, D, x_2000)
```
