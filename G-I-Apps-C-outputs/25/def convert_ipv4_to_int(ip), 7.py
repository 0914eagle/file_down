
def convert_ipv4_to_int(ip):
    a, b, c, d = map(int, ip.split('.'))
    return (a << 24) + (b << 16) + (c << 8) + d

def convert_int_to_ipv4(num):
    return f"{(num >> 24) & 255}.{(num >> 16) & 255}.{(num >> 8) & 255}.{num & 255}"

def optimize_blacklist(n, subnets):
    blacklisted = set()
    whitelisted = set()
    optimized = set()

    for subnet in subnets:
        sign, ip = subnet.split('-' if subnet[0] == '-' else '+')
        ip = ip.replace('/', '')
        ip_int = convert_ipv4_to_int(ip)

        if sign == '-':
            blacklisted.add(ip_int)
        elif sign == '+':
            whitelisted.add(ip_int)

    for black_ip in blacklisted:
        intersection = False
        for white_ip in whitelisted:
            if black_ip & ((black_ip ^ white_ip) + 1) == black_ip:
                intersection = True
                break
        if intersection:
            return -1

    for black_ip in blacklisted:
        mask = 0xFFFFFFFF
        while mask > 0:
            if (black_ip & mask) in blacklisted:
                optimized.add(black_ip & mask)
            mask >>= 1

    return len(optimized), [convert_int_to_ipv4(ip) + '/32' for ip in sorted(optimized)]

# Example usage
n = 2
subnets = ['-127.0.0.1', '+127.0.0.1/32']
result = optimize_blacklist(n, subnets)
print(result[0])
for subnet in result[1]:
    print(subnet)
```
