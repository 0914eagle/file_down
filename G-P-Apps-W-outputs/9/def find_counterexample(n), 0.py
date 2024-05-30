
def find_counterexample(n):
    for m in range(1, 1001):
        if (n * m + 1) not in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
            return m

# Taking input for n
n = int(input())

# Finding and outputting the counterexample
counterexample = find_counterexample(n)
print(counterexample)
```
