
def reconstruct_arrows(N, K, dancers):
    arrows = [0] * N
    for i in range(N):
        arrows[dancers[i]-1] = i+1
    
    if K % 2 != 0:
        print("Impossible")
        return
    
    for i in range(N):
        current = i
        for _ in range(K//2):
            current = arrows[current]-1
        
        if current != i:
            print("Impossible")
            return

    print(" ".join(map(str, arrows)))

# Read input
N, K = map(int, input().split())
dancers = list(map(int, input().split()))

# Call the function
reconstruct_arrows(N, K, dancers)
