
def find_available_dishes(t, test_cases):
    result = []
    
    for test_case in test_cases:
        m, k = test_case[0]
        portions = test_case[1]
        observations = test_case[2:]

        remaining_portions = list(portions)
        can_run_out = ['N'] * k

        for i in range(m - 1):
            dish, disappointed = observations[i]
            if dish != 0 and not disappointed:
                remaining_portions[dish - 1] -= 1

        for i in range(k):
            if sum(remaining_portions[:i+1]) < m:
                can_run_out[i] = 'Y'

        result.append(''.join(can_run_out))

    return result


# Test the function
t = 2
test_cases = [
    [(3, 4), [2, 3, 2, 1], [(1, 0), (0, 0)],
    [(5, 5), [1, 2, 1, 3, 1], [(3, 0), (0, 0), (2, 1), (4, 0)]
]

output = find_available_dishes(t, test_cases)
for out in output:
    print(out)
```
