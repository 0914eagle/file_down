
import math
X = int(input())
max = 0
for b in range(1, int(math.sqrt(X))+1):
  for p in range(2, int(math.log(X,b))+1):
    if b**p <= X:
      max = b**p
print(max)

