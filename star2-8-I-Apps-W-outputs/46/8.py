
def solve(hotdogs, buns):
    hotdogs.sort()
    buns.sort()
    def find_smallest_packs(hotdogs, buns, hotdogs_bought, buns_bought):
        if len(hotdogs) == 0 or len(buns) == 0:
            return float('inf')
        if hotdogs[0] != buns[0]:
            return float('inf')
        elif len(hotdogs) == 1 and len(buns) == 1:
            return 1
        else:
            buy_first_pack = find_smallest_packs(hotdogs[1:], buns[1:], hotdogs_bought + hotdogs[0], buns_bought + buns[0])
            buy_second_pack = find_smallest_packs(hotdogs[1:], buns, hotdogs_bought + hotdogs[0], buns_bought) + 1
            buy_third_pack = find_smallest_packs(hotdogs, buns[1:], hotdogs_bought, buns_bought + buns[0]) + 1
            return min(buy_first_pack, buy_second_pack, buy_third_pack)
    smallest_packs = find_smallest_packs(hotdogs, buns, 0, 0)
    return smallest_packs if smallest_packs != float('inf') else 'impossible'

