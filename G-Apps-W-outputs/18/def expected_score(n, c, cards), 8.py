
def expected_score(n, c, cards):
    cards.sort()
    
    def dfs(idx, drawn, current_max):
        if drawn == c or idx == n:
            return current_max
        
        # Draw the next card
        draw_card = cards[idx]
        score_draw = draw_card + dfs(idx + 1, drawn + 1, max(current_max, draw_card))
        
        # Skip the next card
        score_skip = dfs(idx + 1, drawn, current_max)
        
        return (score_draw * (n - idx) + score_skip * (idx + 1 - drawn)) / (n - drawn)
    
    return round(dfs(0, 0, 0), 6)

# Input
n, c = map(int, input().split())
cards = list(map(int, input().split()))

# Output
print(expected_score(n, c, cards))
