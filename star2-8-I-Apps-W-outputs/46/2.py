
def equalizeHotdogsBuns(hotdogPacks, bunPacks):
    def makePacksEven(packs):
        counts = {}
        for pack in packs:
            counts[pack] = counts.get(pack, 0) + 1
        totalCount = sum(counts.values())
        for pack, count in counts.items():
            if count * 2 == totalCount:
                return 1
        return 2
    totalPacks = makePacksEven(hotdogPacks) + makePacksEven(bunPacks)
    return totalPacks

