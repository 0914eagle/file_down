ulate_algae_growth(r, D, x_2000):
    x_values = [x_2000]
    for i in range(2000, 2010):
        x_i = r * x_values[-1] - D
        x_values.append(x_i)
    
    for x in x_values[1:]:
        print(x)

# Parse input
input_data = input().split()
r = int(input_data[0])
D = int(input_data[1])
x_2000 = int(input_data[2])

# Calculate and print the growth of algae
calculate_algae_growth(r, D, x_2000)
