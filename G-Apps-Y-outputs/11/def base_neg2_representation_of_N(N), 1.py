
def base_neg2_representation_of_N(N):
    if N == 0:
        return "0"
    
    result = ""
    while N != 0:
        remainder = N % -2
        N = N // -2
        if remainder < 0:
            remainder += 2
            N += 1
        result = str(remainder) + result
    
    return result

# Read input from Standard Input
N = int(input())
print(base_neg2_representation_of_N(N))
