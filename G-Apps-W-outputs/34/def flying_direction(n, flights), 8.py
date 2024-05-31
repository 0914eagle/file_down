
def flying_direction(n, flights):
    s_to_f = f_to_s = 0

    for i in range(n - 1):
        if flights[i] == 'S' and flights[i + 1] == 'F':
            s_to_f += 1
        elif flights[i] == 'F' and flights[i + 1] == 'S':
            f_to_s += 1

    if s_to_f > f_to_s:
        print("YES")
    else:
        print("NO")

# Input
n = int(input())
flights = input().strip()

# Call the function
flying_direction(n, flights)
