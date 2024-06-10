

def solve(N, t, A):
    if t == 1:
        return 7
    
    if t == 2:
        if A[0] > A[1]:
            return 'Bigger'
        elif A[0] == A[1]:
            return 'Equal'
        else:
            return 'Smaller'
    
    if t == 3:
        B = [A[0], A[1], A[2]]
        B.sort()
        return B[1]
    
    if t == 4:
        return sum(A)
    
    if t == 5:
        return sum(filter(lambda x: x % 2 == 0, A))
    
    if t == 6:
        return ''.join([chr(ord('a') + x % 26) for x in A])
    
    if t == 7:
        i = 0
        path = set()
        
        while True:
            if i == N - 1:
                return 'Done'
            elif i < 0 or i >= N:
                return 'Out'
            elif i in path:
                return 'Cyclic'
            else:
                path.add(i)
                i = A[i]
            

