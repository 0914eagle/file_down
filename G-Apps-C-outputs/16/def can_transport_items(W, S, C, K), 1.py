
def can_transport_items(W, S, C, K):
    if K < 2:  # when K is less than 2, it's impossible to transport items without loss
        return "NO"
    if (W > 0 and W <= K) or (S > 0 and S <= K) or (C > 0 and C <= K):
        return "YES"
    return "NO"

# Input processing
input_values = input().strip().split()
W, S, C, K = map(int, input_values)

# Call the function with the input values
result = can_transport_items(W, S, C, K)
print(result)
