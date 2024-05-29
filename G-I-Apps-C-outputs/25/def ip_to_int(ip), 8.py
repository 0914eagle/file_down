
def ip_to_int(ip):
    p = map(int, ip.split('.'))
    return p[0]*2**24 + p[1]*2**16 + p[2]*2**8 + p[3]

def int_to_ip(num):
    return '.'.join(str((num >> i) % 256) for i in [24, 16, 8, 0])

n = int(input())
blacklist = []
whitelist = []
black_dict = {}

for _ in range(n):
    line = input().split()
    ip_range = line[1]
    ip, subnet = ip_range.split('/')
    ip_int = ip_to_int(ip)
    mask = (1 << 32) - (1 << (32 - int(subnet)))
    
    if line[0] == '+':
        whitelist.append((ip_int, mask))
    else:
        blacklist.append((ip_int, mask))
        black_dict[ip_int] = mask

for ip_int, mask in whitelist:
    black_dict[ip_int] = 0

results = []
for ip_int in black_dict:
    mask = black_dict[ip_int]
    if mask != 0 and mask in black_dict.values():
        print(-1)
        break
    elif mask != 0:
        results.append((ip_int, mask))

if len(results) == len(black_dict) - len(whitelist):
    print(len(results))
    for ip_int, mask in results:
        print(int_to_ip(ip_int) + '/' + str(32 - mask.bit_length()))
else:
    min_ip = min(black_dict.keys())
    max_ip = max(black_dict.keys())
    print(1)
    print(int_to_ip(min_ip) + '/' + str(32 - (max_ip - min_ip).bit_length()))
```

