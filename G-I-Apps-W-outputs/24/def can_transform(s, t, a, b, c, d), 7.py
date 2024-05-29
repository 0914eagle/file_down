
def can_transform(s, t, a, b, c, d):
    m = len(s)
    n = len(t)
    
    prefix_s = [0] * (m + 1)
    prefix_t = [0] * (n + 1)
    
    for i in range(1, m + 1):
        prefix_s[i] = prefix_s[i-1] + (s[i-1] == 'A')
    
    for i in range(1, n + 1):
        prefix_t[i] = prefix_t[i-1] + (t[i-1] == 'A')
    
    def count(prefix, l, r):
        return prefix[r] - prefix[l - 1]
    
    def delete_a(l, r):
        return count(prefix_s, l, r)
    
    def delete_b(l, r):
        return count(prefix_t, l, r)
    
    def solve(a, b, c, d):
        if delete_a(a, b) < delete_b(c, d):
            return False
        
        if delete_a(a, b) == delete_b(c, d):
            if delete_a(a, b) % 3 != 0:
                return False
            a_a_count = delete_a(a, b) // 3
            b_a_count = delete_b(c, d)
            for _ in range(a_a_count):
                new_s = s.replace('AAB', 'B', 1).replace('BAA', 'C', 1).replace('AAC', 'D', 1)
                s, temp = new_s, s
                
            return s[a:b+1] == t[c:d+1]
        
        return True

    q = int(input())
    result = ''
    for _ in range(q):
        a_i, b_i, c_i, d_i = map(int, input().split())
        res = solve(a_i, b_i, c_i, d_i)
        result += '1' if res else '0'
    
    return result

s = input().strip()
t = input().strip()
print(can_transform(s, t, 0, len(s)-1, 0, len(t)-1))
```
