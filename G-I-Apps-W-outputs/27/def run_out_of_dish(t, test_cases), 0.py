
def run_out_of_dish(t, test_cases):
    result = []
    
    for _ in range(t):
        m, k = test_cases[_][0]
        portions = test_cases[_][1]
        observations = test_cases[_][2:]
        
        remaining_portions = portions[:]
        for obs in observations:
            dish, disappointed = obs
            if dish != 0 and not disappointed:
                remaining_portions[dish-1] -= 1
        
        outcome = ''
        for i in range(k):
            if remaining_portions[i] < m - sum(observations[j][1] for j in range(m-1) if observations[j][0] == 0):
                outcome += 'Y'
            else:
                outcome += 'N'
        
        result.append(outcome)
    
    return result

# Input parsing function
def parse_input(input_string):
    input_lines = input_string.strip().split('\n')
    t = int(input_lines[0])
    
    test_cases = []
    current_line = 1
    for _ in range(t):
        m, k = map(int, input_lines[current_line].split())
        portions = list(map(int, input_lines[current_line + 1].split()))
        observations = [list(map(int, line.split())) for line in input_lines[current_line + 2:current_line + m]]
        
        test_cases.append([(m, k), portions] + observations)
        current_line += m + 2
    
    return t, test_cases

# Example usage with the provided example input
input_str = '''2
3 4
2 3 2 1
1 0
0 0
5 5
1 2 1 3 1
3 0
0 0
2 1
4 0'''

t, test_cases = parse_input(input_str)
output = run_out_of_dish(t, test_cases)
for line in output:
    print(line)
