
from sys import stdin

def solve(n, q, operations):
    if n == 1:
        return 0
    
    combinations = {}
    
    for _ in range(q):
        a, b = next(stdin).split()
        
        combinations.setdefault(a, set()).add(b)
    
    def build_strings(length):
        if length == 1:
            return ['a', 'b', 'c', 'd', 'e', 'f']
        
        strings = []
        
        for s in build_strings(length - 1):
            for c in 'abcdef':
                strings.append(s + c)
        
        return strings
    
    def count_strings(strings):
        count = 0
        
        for s in strings:
            if len(s) == 1:
                if s == 'a':
                    count += 1
            else:
                for c in combinations.get(s[:2], []):
                    count += count_strings([s[2:] + c])
        
        return count
    
    return count_strings(build_strings(n))


n, q = map(int, next(stdin).split())
operations = [next(stdin).split() for _ in range(q)]

print(solve(n, q, operations))

