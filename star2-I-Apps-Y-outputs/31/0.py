
def best_card(G, S, C):
    buying_power = 3*G + 2*S + C
    if buying_power >= 8:
        return "Province"
    elif buying_power >= 5:
        return "Duchy"
    elif buying_power >= 2:
        return "Estate"
    else:
        return ""

def best_treasure(G, S, C):
    buying_power = 3*G + 2*S + C
    if buying_power >= 6:
        return "Gold"
    elif buying_power >= 3:
        return "Silver"
    elif buying_power >= 1:
        return "Copper"
    else:
        return ""

def main():
    G, S, C = map(int, input().split())
    victory_card = best_card(G, S, C)
    treasure_card = best_treasure(G, S, C)
    if victory_card:
        print(victory_card + " or " + treasure_card)
    else:
        print(treasure_card)

if __name__ == "__main__":
    main()

