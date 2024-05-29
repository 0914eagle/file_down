
def optimize_blacklist(n, subnets):
    blacklist = set()
    whitelist = set()
    
    for subnet in subnets:
        is_blacklist, address = subnet[0], subnet[1]
        if is_blacklist == '-':
            blacklist.add(address)
        else:
            whitelist.add(address)
    
    overlap = blacklist.intersection(whitelist)
    if overlap:
        return -1
    
    optimized_blacklist = []
    for subnet in blacklist:
        parts = subnet.split('/')
        prefix = parts[0]
        prefix_bin = ''.join(format(int(x), '08b') for x in prefix.split('.'))
        if len(parts) == 1:
            optimized_blacklist.append(prefix_bin + '/32')
        else:
            x = int(parts[1])
            start = list(prefix_bin)
            for i in range(32 - x, 32):
                start[i] = '0'
            startsubnet = ''.join(start)
            optimized_blacklist.append(startsubnet + '/' + str(x))
    
    return len(optimized_blacklist), optimized_blacklist

# Input parsing
n = int(input())
subnets = [input().split()[1] for _ in range(n)]

# Output
result = optimize_blacklist(n, subnets)
if result == -1:
    print(-1)
else:
    t, optimized_blacklist = result
    print(t)
    for subnet in optimized_blacklist:
        print(subnet)
```
