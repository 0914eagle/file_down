
def max_lemonade(N, offers):
    class Exchange:
        def __init__(self, rate, offer, want):
            self.rate = rate
            self.offer = offer
            self.want = want

    exchanges = [Exchange(rate, offer, want) for offer, want, rate in offers]
    exchanges.sort(key=lambda x: x.rate, reverse=True)

    max_blue_lemonade = 0
    blue_lemonade = 1
    for exchange in exchanges:
        if exchange.want == "pink":
            continue
        if exchange.offer == "blue":
            max_blue_lemonade += exchange.rate * blue_lemonade
        elif exchange.offer == "pink":
            if exchange.rate < 1:
                max_blue_lemonade += blue_lemonade
            else:
                blue_lemonade *= exchange.rate

    return min(max_blue_lemonade, 10)
N = int(input())
offers = [input().split() for _ in range(N)]
print(max_lemonade(N, offers))

