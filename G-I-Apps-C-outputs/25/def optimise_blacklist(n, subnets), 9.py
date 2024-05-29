
import ipaddress

def optimise_blacklist(n, subnets):
    blacklist = set()
    whitelist = set()
    
    for subnet in subnets:
        if subnet[0] == '-':
            blacklist.add(ipaddress.ip_network(subnet[1]))
        else:
            whitelist.add(ipaddress.ip_network(subnet[1]))
    
    conflicting_address = False
    for addr in whitelist:
        if any(addr.overlaps(black_subnet) for black_subnet in blacklist):
            conflicting_address = True
            break
    
    if conflicting_address:
        print(-1)
    else:
        optimized_blacklist = set()
        for black_subnet in blacklist:
            add_to_optimized = True
            for whit_subnet in whitelist:
                if whit_subnet.subnet_of(black_subnet):
                    add_to_optimized = False
                    break
                
            if add_to_optimized:
                optimized_blacklist.add(black_subnet)
        
        print(len(optimized_blacklist))
        for subnet in optimized_blacklist:
            print(str(subnet))

# Example usage
n = 4
subnets = [
    ("-149.154.167.99",),
    ("+149.154.167.100/30",),
    ("+149.154.167.128/25",),
    ("-149.154.167.120/29",)
]

optimise_blacklist(n, subnets)
