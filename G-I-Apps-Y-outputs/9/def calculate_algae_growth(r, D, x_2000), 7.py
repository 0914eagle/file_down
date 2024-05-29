
# Function to calculate algae development based on given parameters
def calculate_algae_growth(r, D, x_2000):
    x_values = [x_2000]
    for i in range(1, 11):
        x_next = r * x_values[i-1] - D
        x_values.append(x_next)
    
    # Printing the results
    for x in x_values[1:]:
        print(int(x))

# Parsing input values
r, D, x_2000 = map(int, input().split())

# Calling the function
calculate_algae_growth(r, D, x_2000)
```
