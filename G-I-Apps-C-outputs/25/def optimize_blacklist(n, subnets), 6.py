
def optimize_blacklist(n, subnets):
    whitelist = set()
    blacklist = set()
    
    for subnet in subnets:
        if subnet[0] == '+':
            whitelist.add(subnet[1])
        else:
            blacklist.add(subnet[1])
    
    intersection = whitelist.intersection(blacklist)
    if intersection:
        print("-1")
        return
    
    blacklist_cidr = convert_to_cidr(blacklist)
    
    print(len(blacklist_cidr))
    for subnet in blacklist_cidr:
        print(subnet)

def convert_to_cidr(subnets):
    subnets = sorted(subnets)
    result = []
    
    while subnets:
        cur_subnet = subnets.pop(0)
        ip, mask = cur_subnet.split('/')
        
        for i, subnet in enumerate(subnets):
            next_ip, next_mask = subnet.split('/')
            
            if ip == next_ip[:len(ip)] and int(next_mask) > int(mask):
                subnets.pop(i)
        
        result.append(cur_subnet)
    
    return result

# Input parsing
n = int(input())
subnets = [input().split() for _ in range(n)]

optimize_blacklist(n, subnets)
```
