
def check_healths(N, S):
    S.sort(reverse=True)
    
    if N == 0:
        return "Yes" if S[0] == 1 else "No"
    
    if len(S) < 2:
        return "No"
    
    root = S[0]
    S.remove(root)
    
    for i in range(1 << N):
        child = root - i
        if child <= 0:
            return "No"
        
        if child in S:
            S.remove(child)
        else:
            return "No"
    
    return "Yes"

# Input processing
N = int(input())
S = list(map(int, input().split()))

# Call the function and print the output
print(check_healths(N, S))
