
def shortest_time_skis(W, v_h, N, gates, S, skis):
    def time_to_reach_gate(x1, y1, x2, y2, v_ski, v_h):
        return (y2 - y1) / v_ski + abs(x2 - x1) / v_h

    def can_pass_through_all_gates(v_ski):
        t = 0
        for i in range(N-1):
            x1, y1 = gates[i]
            x2, y2 = gates[i+1]
            time_to_gate = time_to_reach_gate(x1, y1, x2, y2, v_ski, v_h)
            t += time_to_gate
            if t > (y2 - y1) / v_ski:
                return False
        return True

    min_time = float('inf')
    min_ski = None
    for ski in skis:
        if can_pass_through_all_gates(ski):
            t = gates[-1][1] / ski
            if t < min_time:
                min_time = t
                min_ski = ski

    if min_ski:
        return min_ski
    else:
        return "IMPOSSIBLE"

# Sample Input Parsing
input_vals = input().strip().split()
W, v_h, N = map(int, input_vals)
gates = []
for _ in range(N):
    x, y = map(int, input().strip().split())
    gates.append((x, y))
S = int(input())
skis = [int(input()) for _ in range(S)]

# Call the function and print the output
result = shortest_time_skis(W, v_h, N, gates, S, skis)
print(result)
