
def find_absent_gems():
    gems_colors = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind"
    }
    
    gem_colors_seen = set()
    for _ in range(int(input())):
        gem_colors_seen.add(input().strip())
    
    missing_gems = set(gems_colors.keys()) - gem_colors_seen
    print(len(missing_gems))
    for color in missing_gems:
        print(gems_colors[color])

find_absent_gems()
