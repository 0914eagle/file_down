
import ipaddress

def merge_subnets(blacklist, whitelist):
    merged = []
    
    black_ips = set()
    white_ips = set()
    
    for sub in blacklist:
        black_ips.update(ipaddress.IPv4Network(sub).hosts())
    
    for sub in whitelist:
        white_ips.update(ipaddress.IPv4Network(sub).hosts())
    
    if black_ips & white_ips:
        return -1
    
    for ip in black_ips:
        a, b, c, d = str(ip).split('.')
        mask = 32
        
        while mask > 0:
            subnet = f'{a}.{b}.{c}.{d}/{mask}'
            subnet_ip = ipaddress.IPv4Network(subnet, strict=False)
            
            if any(ip in subnet_ip for ip in black_ips):
                merged.append(subnet)
                black_ips -= set(subnet_ip.hosts())
            mask -= 1
    
    return len(merged), merged

# Input parsing
n = int(input())
blacklist = []
whitelist = []

for _ in range(n):
    line = input().split()
    if line[0] == '-':
        blacklist.append(line[1])
    else:
        whitelist.append(line[1])

# Call merge_subnets function
result = merge_subnets(blacklist, whitelist)

# Output formatting
if result == -1:
    print(-1)
else:
    t, subnets = result
    print(t)
    for subnet in subnets:
        print(subnet)
```

