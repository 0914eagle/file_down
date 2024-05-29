
def can_transform(S, T, a, b, c, d):
    mapping = {'A': 'BC', 'B': 'AC', 'C': 'AB'}
    
    while a <= b and c <= d:
        if S[a-1] != T[c-1]:
            return 0
        
        char = S[a-1]
        
        if char == 'A':
            if S[a] == 'A':
                a += 2
            else:
                a += 1
        elif char == 'B':
            if S[a] == 'B':
                a += 2
            else:
                a += 1
        else:
            if S[a] == 'C':
                a += 2
            else:
                a += 1

        c += 1

    return 1

input_S = input().strip()
input_T = input().strip()
Q = int(input())

result = ''
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    result += str(can_transform(input_S, input_T, a, b, c, d))

print(result)
