
def valera_marathon(a, d, n):
    x, y = 0, 0
    for i in range(1, n + 1):
        drink_x = (i * d) % a
        drink_y = min((i * d) // a, a)
        
        if drink_x <= a / 2:
            x = drink_x
            y = drink_y
        else:
            x = a - drink_y
            y = a - drink_x
        
        print("{:.10f} {:.10f}".format(x, y))

# Read input
a, d = map(float, input().split())
n = int(input())

# Call the function with input values
valera_marathon(a, d, n)
