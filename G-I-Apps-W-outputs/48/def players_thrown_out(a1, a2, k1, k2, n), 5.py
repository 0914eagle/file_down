
def players_thrown_out(a1, a2, k1, k2, n):
    min_thrown_out = max(0, n - (a1*(k1-1) + a2*(k2-1)))
    
    max_thrown_out = min(min(a1, n//k1), a1 + a2 - (n - a1*(k1-1))//k2)
    
    print(min_thrown_out, max_thrown_out)

# Input
a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())

players_thrown_out(a1, a2, k1, k2, n)
