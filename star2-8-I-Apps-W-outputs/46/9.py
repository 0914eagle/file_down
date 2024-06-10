
def get_packs(hotdogs, buns):
    for hotdog_pack in hotdogs:
        for bun_pack in buns:
            if hotdog_pack == bun_pack:
                return 1, 1
    for hotdog_pack in hotdogs:
        for bun_pack in buns:
            if hotdog_pack + bun_pack == hotdog_pack:
                return 1, 2
            elif hotdog_pack + bun_pack == bun_pack:
                return 2, 1
    for i, hotdog_pack1 in enumerate(hotdogs):
        for j, hotdog_pack2 in enumerate(hotdogs):
            for k, bun_pack1 in enumerate(buns):
                for l, bun_pack2 in enumerate(buns):
                    if i != j and k != l and hotdog_pack1 + hotdog_pack2 == bun_pack1 + bun_pack2:
                        return 2, 2
    return "impossible"

if __name__ == '__main__':
    n_hotdogs = int(input())
    hotdogs = [int(x) for x in input().split()]
    n_buns = int(input())
    buns = [int(x) for x in input().split()]
    answer = get_packs(hotdogs, buns)
    if answer == "impossible":
        print("impossible")
    else:
        print(answer[0] + answer[1])

