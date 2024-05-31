
def solve_infinity_gauntlet():
    gems = {
        "purple": "Power",
        "green": "Time",
        "blue": "Space",
        "orange": "Soul",
        "red": "Reality",
        "yellow": "Mind"
    }

    n = int(input())
    seen_gems = set()
    
    for _ in range(n):
        color = input().strip()
        seen_gems.add(gems[color])

    missing_gems = set(gems.values()) - seen_gems

    print(len(missing_gems))
    for gem in missing_gems:
        print(gem)

solve_infinity_gauntlet()
