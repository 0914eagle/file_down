
def can_run_out_dishes(t, sets):
    results = []
    
    for _ in range(t):
        m, k = sets[_][0]
        a = sets[_][1]
        observations = sets[_][2:]
        
        remaining = a[:]
        disappointed = [False] * k
        
        for obs in observations:
            idx, dis = obs
            if idx > 0 and not disappointed[idx - 1]:
                remaining[idx - 1] -= 1
                if remaining[idx - 1] == 0:
                    disappointed[idx - 1] = True
        
        res = []
        for i in range(k):
            if i == a.index(max(a)):
                res.append('N')
            elif remaining[i] >= (m - sum(disappointed)):
                res.append('N')
            else:
                res.append('Y')
        
        results.append(''.join(res))
    
    for result in results:
        print(result)


# Example input
t = 2
sets = [
    [(3, 4), [2, 3, 2, 1], [1, 0], [0, 0]],
    [(5, 5), [1, 2, 1, 3, 1], [3, 0], [0, 0], [2, 1], [4, 0]]
]

can_run_out_dishes(t, sets)
```
