
def run_out_of_dish(t, test_cases):
    result = []

    for _ in range(t):
        m, k = test_cases[_][0]
        a = test_cases[_][1]
        observations = test_cases[_][2:]

        count_left = list(a)
        disappointed = set()

        for i in range(m - 1):
            t_j, r_j = observations[i]
            if t_j != 0 and r_j == 0:
                disappointed.add(t_j)

        for dish in disappointed:
            count_left[dish - 1] -= 1

        output = ""
        for left in count_left:
            if left >= m - len(disappointed):
                output += "N"
            else:
                output += "Y"
        
        result.append(output)

    return result


# Input parsing
t = int(input())
test_cases = []

for _ in range(t):
    input()
    m, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    observations = []
    for _ in range(m - 1):
        t_j, r_j = map(int, input().split())
        observations.append((t_j, r_j))

    test_cases.append((m, k, a, observations))

# Function call
output = run_out_of_dish(t, test_cases)

# Output
for line in output:
    print(line)
```
