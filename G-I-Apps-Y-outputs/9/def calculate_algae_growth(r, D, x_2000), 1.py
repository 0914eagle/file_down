
def calculate_algae_growth(r, D, x_2000):
    x_values = [x_2000]
    for i in range(2000, 2010):
        x_next = r * x_values[-1] - D
        x_values.append(x_next)

    for x in x_values[1:]:
        print(x)

r, D, x_2000 = map(int, input().split())
calculate_algae_growth(r, D, x_2000)
```
