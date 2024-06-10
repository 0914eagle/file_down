
from sys import stdin

class Deck:
    def __init__(self, size):
        self.size = size
        self.top_idx = 0
    
    def draw(self):
        if self.top_idx == self.size:
            return None
        card = self.top_idx
        self.top_idx += 1
        return card
    
    def discard(self, card):
        pass
    
    def __repr__(self):
        return f"Deck(size={self.size}, top_idx={self.top_idx})"


class Player:
    def __init__(self, id, deck, exploding_kittens, defuses):
        self.id = id
        self.deck = deck
        self.exploding_kittens = exploding_kittens
        self.defuses = defuses
        self.hand = []
    
    def take_turn(self):
        card = self.deck.draw()
        if card is None:
            return False
        
        self.hand.append(card)
        
        if card in self.exploding_kittens:
            self.exploding_kittens.remove(card)
            if card in self.defuses:
                self.defuses.remove(card)
                self.deck.discard(card)
            else:
                self.deck.discard(card)
                return False
        
        if len(self.hand) > 5:
            self.hand = self.hand[:5]
        
        return True
    
    def __repr__(self):
        return f"Player(id={self.id}, deck={self.deck}, hand={self.hand})"


def main():
    players = []
    
    n, e, d = map(int, stdin.readline().split())
    
    exploding_kittens = sorted(map(int, stdin.readline().split()))
    defuses = sorted(map(int, stdin.readline().split()))
    
    deck = Deck(e + d)
    
    for i in range(n):
        player = Player(i, deck, exploding_kittens, defuses)
        players.append(player)
    
    rounds = 0
    
    while True:
        for player in players:
            if not player.take_turn():
                return player.id
        
        rounds += 1


if __name__ == "__main__":
    print(main())

