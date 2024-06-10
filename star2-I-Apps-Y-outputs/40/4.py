
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

def ceil(a, b):
    return (a + b - 1) // b

t = 0
t += ceil(t, 10)
t += A
t += ceil(t, 10)
t += B
t += ceil(t, 10)
t += C
t += ceil(t, 10)
t += D
t += ceil(t, 10)
t += E
print(t)

