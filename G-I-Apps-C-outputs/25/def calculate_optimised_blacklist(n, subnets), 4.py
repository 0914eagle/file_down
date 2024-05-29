
import ipaddress

def calculate_optimised_blacklist(n, subnets):
    blacklist = set()
    whitelist = set()
    optimised_blacklist = set()

    for subnet in subnets:
        if subnet[0] == '-':
            blacklist.add(ipaddress.ip_network(subnet[1], strict=False))
        else:
            whitelist.add(ipaddress.ip_network(subnet[1], strict=False))

    for b_subnet in blacklist:
        for w_subnet in whitelist:
            if b_subnet.overlaps(w_subnet):
                return -1

    blacklist = list(blacklist)
    whitelist = list(whitelist)

    for b_subnet in blacklist:
        contained = False
        for ob_subnet in optimised_blacklist:
            if b_subnet.subnet_of(ob_subnet):
                contained = True
                break
            elif b_subnet.supernet_of(ob_subnet):
                optimised_blacklist.remove(ob_subnet)

        if not contained:
            optimised_blacklist.add(b_subnet)

    return len(optimised_blacklist), [str(subnet) for subnet in optimised_blacklist]

# Example inputs
input1 = [
    "-149.154.167.99",
]

input2 = [
    "-149.154.167.99",
    "+149.154.167.100/30",
    "+149.154.167.128/25",
    "-149.154.167.120/29",
]

print(calculate_optimised_blacklist(len(input1), input1))
print(calculate_optimised_blacklist(len(input2), input2))
