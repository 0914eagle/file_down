
def check_transitions(S, T, queries):
    def apply_transitions(string):
        while True:
            change = False
            if 'AAA' in string:
                string = string.replace('AAA', '')
                change = True
            if 'A' in string and 'BC' in string:
                string = string.replace('A', '')
                string = string.replace('BC', 'A')
                change = True
            if 'B' in string and 'AC' in string:
                string = string.replace('B', '')
                string = string.replace('AC', 'B')
                change = True
            if 'C' in string and 'AB' in string:
                string = string.replace('C', '')
                string = string.replace('AB', 'C')
                change = True
            if not change:
                break
        return string

    result = ''
    for query in queries:
        substring_S = S[query[0]-1:query[1]]
        substring_T = T[query[2]-1:query[3]
        transformed_S = apply_transitions(substring_S)
        result += '1' if transformed_S == substring_T else '0'

    return result

# Input
S = input().strip()
T = input().strip()
Q = int(input().strip())

queries = []
for _ in range(Q):
    a, b, c, d = map(int, input().strip().split())
    queries.append((a, b, c, d))

# Output
print(check_transitions(S, T, queries))
