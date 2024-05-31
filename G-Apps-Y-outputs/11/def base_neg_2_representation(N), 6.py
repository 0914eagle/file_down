
def base_neg_2_representation(N):
    if N == 0:
        return "0"
    
    result = ""
    while N != 0:
        remainder = N % -2
        N //= -2
        
        if remainder < 0:
            remainder += 2
            N += 1
        
        result = str(remainder) + result
    
    return result

# Input
N = int(input())
# Output
print(base_neg_2_representation(N))
