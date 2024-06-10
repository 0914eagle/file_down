
def best_card(g, s, c):
    victory_points = [6, 3, 1]
    buying_power = [3, 2, 1]
    victory_cards = ["Province", "Duchy", "Estate"]
    treasure_cards = ["Gold", "Silver", "Copper"]
    
    best_victory_card = None
    best_victory_points = 0
    
    best_treasure_card = None
    best_buying_power = 0
    
    for i in range(3):
        if victory_points[i] <= g + s + c:
            if victory_points[i] > best_victory_points:
                best_victory_card = victory_cards[i]
                best_victory_points = victory_points[i]
        
        if buying_power[i] <= g + s + c:
            if buying_power[i] > best_buying_power:
                best_treasure_card = treasure_cards[i]
                best_buying_power = buying_power[i]
    
    if best_victory_card is None:
        return best_treasure_card
    
    if best_treasure_card is None:
        return best_victory_card
    
    return best_victory_card + " or " + best_treasure_card

g, s, c = map(int, input().split())
print(best_card(g, s, c))

