
 def solve(N):
    binary = bin(N)[2:]
    return ''.join([str(int(i)) for i in binary])
 