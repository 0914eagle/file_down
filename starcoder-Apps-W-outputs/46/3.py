
import numpy as np

n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

a_new = np.array(a)
print(np.sum(a_new))
