
def best_victory_and_treasure(gold, silver, copper):
    buying_power = 2 * gold + 2 * silver + 1 * copper
    if buying_power >= 8:
        return "Province"
    elif buying_power >= 5:
        return "Duchy"
    elif buying_power >= 2:
        return "Estate"
    else:
        return ""

def best_treasure(gold, silver, copper):
    buying_power = 2 * gold + 2 * silver + 1 * copper
    if buying_power >= 6:
        return "Gold"
    elif buying_power >= 3:
        return "Silver"
    else:
        return "Copper"

def main():
    g, s, c = map(int, input().split())
    victory = best_victory_and_treasure(g, s, c)
    treasure = best_treasure(g, s, c)
    if victory:
        print(victory + " or " + treasure)
    else:
        print(treasure)

if __name__ == "__main__":
    main()

