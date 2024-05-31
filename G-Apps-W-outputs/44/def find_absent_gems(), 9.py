
def find_absent_gems():
    colors = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind"
    }
    
    n = int(input())
    gems_seen = set()
    
    for _ in range(n):
        gems_seen.add(input())
    
    gems_absent = set(colors.values()) - set([colors[color] for color in gems_seen])
    
    m = len(gems_absent)
    print(m)
    
    for gem in gems_absent:
        print(gem)

find_absent_gems()
