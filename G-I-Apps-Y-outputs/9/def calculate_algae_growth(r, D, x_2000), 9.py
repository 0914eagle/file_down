
def calculate_algae_growth(r, D, x_2000):
    x_values = []
    
    for i in range(10):
        x_i = r * x_2000 - D
        x_values.append(x_i)
        x_2000 = x_i

    for x in x_values:
        print(x)

# Input processing
input_values = input().split()
r = int(input_values[0])
D = int(input_values[1])
x_2000 = int(input_values[2])

calculate_algae_growth(r, D, x_2000)
```
