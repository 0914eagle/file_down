
import itertools

def subnet_to_range(subnet):
    if '/' in subnet:
        ip, suffix = subnet.split('/')
        suffix = int(suffix)
        ip_num = sum(int(octet)*(256**(3-i)) for i, octet in enumerate(ip.split('.')))
        start = ip_num & ~(2**(32-suffix)-1)
        end = ip_num | (2**(32-suffix)-1)
        return range(start, end+1)
    else:
        ip_num = sum(int(octet)*(256**(3-i)) for i, octet in enumerate(subnet.split('.')))
        return [ip_num]

def merge_ranges(ranges):
    ranges = sorted(set(itertools.chain(*ranges)))
    start = ranges[0]
    end = ranges[0]
    result = []
    for num in ranges[1:]:
        if num == end + 1:
            end = num
        else:
            result.append((start, end))
            start = num
            end = num
    result.append((start, end))
    return result

def optimize_blacklist(n, subnets):
    whitelist = []
    blacklist = []
    
    for subnet in subnets:
        if subnet[0] == '+':
            whitelist.extend(subnet_to_range(subnet[1:]))
        else:
            blacklist.extend(subnet_to_range(subnet[1:]))
    
    for ip in whitelist:
        if ip in blacklist:
            return -1
    
    combined_ranges = merge_ranges([blacklist])
    
    return len(combined_ranges), [f"{start // 2**24}.{(start // 2**16) % 256}.{(start // 2**8) % 256}.{start % 256}/{32-(start & -start).bit_length()}" for start, end in combined_ranges]

# Input handling
n = int(input())
subnets = [input().strip() for _ in range(n)]

# Output
result = optimize_blacklist(n, subnets)
if result == -1:
    print(result)
else:
    print(result[0])
    for subnet in result[1]:
        print(subnet)
```

