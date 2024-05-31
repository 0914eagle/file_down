
def reconstruct_arrows(N, K, dancers):
    arrows = [0] * N
    for i in range(N):
        arrows[dancers[i]-1] = i+1
    
    if K % 2 != 0:
        print("Impossible")
        return
    
    for i in range(N):
        if dancers[arrows[i]-1] != i+1:
            print("Impossible")
            return
    
    for i in range(N):
        print(arrows[i], end=' ')
    print()

# Read input
N, K = map(int, input().split())
dancers = list(map(int, input().split()))

# Call the function with input values
reconstruct_arrows(N, K, dancers)
