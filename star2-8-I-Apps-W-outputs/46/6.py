
h, *hlist = map(int, input().split())
b, *blist = map(int, input().split())

result = 99999999
for hpack in range(0, h+1):
    for bpack in range(0, b+1):
        if hlist.count(hpack) > 0 and blist.count(bpack) > 0:
            if hpack + bpack < result and hlist.count(hpack) >= 1 and blist.count(bpack) >= 1:
                result = hpack + bpack

if result == 99999999:
    print("impossible")
else:
    print(result)

