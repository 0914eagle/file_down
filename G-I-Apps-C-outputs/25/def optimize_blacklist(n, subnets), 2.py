
def optimize_blacklist(n, subnets):
    blacklisted = set()
    whitelisted = set()
    optimized_blacklist = set()

    for subnet in subnets:
        is_blacklist, address = subnet.split('.')
        if is_blacklist == '-':
            blacklisted.add(address)
        else:
            whitelisted.add(address)

    for subnet in blacklisted:
        if subnet in whitelisted:
            return -1

    blacklisted = sorted(list(blacklisted))

    for subnet in blacklisted:
        parts = subnet.split('.')
        for i in range(32):
            mask = (1 << i) - 1
            sub_address = '.'.join(parts[:i]) + '.0.0' + '/' + str(32-i)
            optimized_blacklist.add(sub_address)

    return len(optimized_blacklist), optimized_blacklist
