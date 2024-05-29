
def ip_to_int(ip):
    a, b, c, d = map(int, ip.split('.'))
    return (a << 24) + (b << 16) + (c << 8) + d

def int_to_ip(num):
    a = (num >> 24) & 255
    b = (num >> 16) & 255
    c = (num >> 8) & 255
    d = num & 255
    return f"{a}.{b}.{c}.{d}"

def optimize_blacklist(n, subnets):
    whitelist = set()
    blacklist = set()
    for subnet in subnets:
        if subnet[0] == '+':
            whitelist.add(subnet[1])
        else:
            blacklist.add(subnet[1])

    for ip in whitelist.intersection(blacklist):
        return -1

    blacklist_ranges = []
    for subnet in blacklist:
        ip_integer, mask = subnet.split('/')
        ip_integer = ip_to_int(ip_integer)
        mask = int(mask) if '/' in subnet else 32

        start_ip = ip_integer & ((2**32 - 1) << (32 - mask))
        end_ip = start_ip + 2**(32 - mask) - 1
        blacklist_ranges.append((start_ip, end_ip))

    blacklist_ranges.sort()

    minimized_blacklist = []
    current_start, current_end = blacklist_ranges[0]
    for start, end in blacklist_ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            minimized_blacklist.append((current_start, current_end))
            current_start, current_end = start, end
    minimized_blacklist.append((current_start, current_end))

    return len(minimized_blacklist), [int_to_ip(start) + '/' + str(32 - (end - start).bit_length()) if start != end else int_to_ip(start) for start, end in minimized_blacklist]

# Input parsing
n = int(input())
subnets = [input().split() for _ in range(n)]

# Call the function and print the output
output = optimize_blacklist(n, subnets)
if output == -1:
    print(-1)
else:
    print(output[0])
    for subnet in output[1]:
        print(subnet)
```

